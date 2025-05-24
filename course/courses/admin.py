from django.contrib import admin, messages
from django.db.models import Count
from django.core.exceptions import ValidationError

from .models import Course, Lecturer, CourseLecturer


class CourseLecturerInline(admin.TabularInline):
    model = CourseLecturer
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseLecturerInline]
    exclude = ('creator',)

    def has_add_permission(self, request):
        lecturer = Lecturer.objects.filter(user=request.user).first()
        return bool(lecturer and lecturer.type == "P")

    def save_model(self, request, obj, form, change):
        obj.creator = request.user

        # Проверка дали курсот веќе постои со исто име
        if not change and Course.objects.filter(name=obj.name).exists():
            messages.warning(request, "Веќе постои курс со тоа име.")
            return

        super().save_model(request, obj, form, change)




    def has_change_permission(self, request, obj=None):
        return obj and obj.creator == request.user

    def has_delete_permission(self, request, obj=None):
        return obj and obj.creator == request.user

    def get_queryset(self, request):
        return Course.objects.filter(creator=request.user)


class LecturerAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(courseCount=Count('courses')).filter(courseCount__lt=2)
        return qs
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class CourseLecturerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Секој предавач може да учествува на најмногу 3 курса истовремено.
        if not change and obj.lecturer.courses.all().count() >= 3:
            messages.warning(request, "This lecturer cant have more than 3 courses")
            return

        existing_courses = CourseLecturer.objects.select_related('course') \
            .filter(lecturer=obj.lecturer).exclude(course=obj.course)

        total_days = sum(
            (cl.course.end_date - cl.course.start_date).days
            for cl in existing_courses
            if cl.course.start_date and cl.course.end_date
        )

        new_course_duration = (
                    obj.course.end_date - obj.course.start_date).days if obj.course.start_date and obj.course.end_date else 0

        if total_days + new_course_duration > 365:
            messages.error(request,
                           f"Вкупната должина на курсевите за предавачот не смее да надмине 365 дена. Сега е: {total_days + new_course_duration}")
            return

        super().save_model(request, obj, form, change)


# ✅ Регистрација на моделите
admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(CourseLecturer, CourseLecturerAdmin)
