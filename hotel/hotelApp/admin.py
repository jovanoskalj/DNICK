from django.contrib import admin
from .models import *


# При креирањето на резервацијата, корисникот се доделува автоматски според
# најавениот
# корисник во моментот на системот. Не треба да се дозволи резервирање на
# соба која не е
# исчистена.

# Register your models here.
class RoomHygienistInline(admin.TabularInline):
    model = RoomHygienist
    extra = 0


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [RoomHygienistInline, ]
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(EmployeeAdmin, self).save_model(request, obj, form, change)


class ReservationAdmin(admin.ModelAdmin):
    exclude = ('guest',)
    list_display = ('code', 'room',)

    def save_model(self, request, obj, form, change):
        obj.guest = request.user
        room = Room.objects.filter(room_number=obj.room.room_number, isCleaned=True).exists()
        if not room and not change:
            return

        return super(ReservationAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True  # дозволи пристап до листата на објекти

        if obj.guest == request.user:
            return True

        if obj.receptionist and obj.receptionist.type in ['R', 'M']:
            return True

        return False


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'isCleaned',)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return obj and Employee.objects.filter(user=request.user, type='H').exists()


admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Employee, EmployeeAdmin)
# admin.site.register(Employee, EmployeeAdmin)
