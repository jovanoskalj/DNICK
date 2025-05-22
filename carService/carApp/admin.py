from django.contrib import admin
from .models import *

# Register your models here.

class ServicePlaceManufacturerInline(admin.TabularInline):
    extra = 0
    model = ServicePlaceManufacturer

class ServicePlaceAdmin(admin.ModelAdmin):
    inlines = [ServicePlaceManufacturerInline, ]

    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

class ServiceAdmin(admin.ModelAdmin):
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ServiceAdmin, self).save_model(request, obj, form, change)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    def has_add_permission(self, request):
        return request.user.is_superuser

class CarAdmin(admin.ModelAdmin):
    list_display = ('type','max_speed')



admin.site.register(Car,CarAdmin)
admin.site.register(Manufacturer,ManufacturerAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(ServicePlace,ServicePlaceAdmin)
# admin.site.register(ServicePlaceManufacturer,ServicePlaceManufacturerInline)