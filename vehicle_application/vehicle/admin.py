from django.contrib import admin
from .models import Manufacturer, Car


class ManufacturerAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    list_display = ('name', 'location', 'year_of_establishment', 'num_employees', 'user')

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        return Car.objects.filter(user=request.user)


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'manufacturer', 'model', 'price', 'year_of_production', 'mileage', 'color', 'type', 'chassis_number')

    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
