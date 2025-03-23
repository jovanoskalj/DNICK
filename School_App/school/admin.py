from django.contrib import admin
from .models import *

# Предметите се додаваат во делот за училишта.
class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 0

class SchoolAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]
    exclude = ["added_by",]

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(SchoolAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if obj and obj.added_by == request.user:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.added_by == request.user:
            return True
        return False

class TeacherAdmin(admin.ModelAdmin):
    exclude = ["added_by", ]

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(TeacherAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.added_by == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.added_by == request.user:
            return True
        return False

class StudentAdmin(admin.ModelAdmin):
    exclude = ["added_by", ]
    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(StudentAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.added_by == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.added_by == request.user:
            return True
        return False

class SubjectAdmin (admin.ModelAdmin):
    list_filter = ["grade",]

# Регистрирај ги моделите со нивните Admin конфигурации
admin.site.register(School, SchoolAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(TeacherSubject)
admin.site.register(Address)
