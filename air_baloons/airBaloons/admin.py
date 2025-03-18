from django.contrib import admin
from .models import *



# Register your models here.
class AirlinePilotInline(admin.TabularInline):
    model = PilotAirline
    extra = 1


class FlightAdmin(admin.ModelAdmin):
    exclude = ("added_by",)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(FlightAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user == obj.added_by
    def has_delete_permission(self, request, obj=None):
        return False

class AirlineAdmin(admin.ModelAdmin):
    inlines = [AirlinePilotInline, ]

    def has_add_permission(self, request):
        return True


admin.site.register (AirBalloon)
admin.site.register (Pilot)
admin.site.register (Flight, FlightAdmin)
admin.site.register (Airline,AirlineAdmin)



