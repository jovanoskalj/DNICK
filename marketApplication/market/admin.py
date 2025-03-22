from django.contrib import admin
from .models import *

# Register your models here.
class ProductMarketInline(admin.TabularInline):
    model = MarketProduct
    extra = 1


class MarketAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [ProductMarketInline]
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        return super(MarketAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:  # Corrected from obj.user
            if request.user.is_superuser:
                return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:  # Corrected from obj.user
            if request.user.is_superuser:
                return True
        return False


class EmployeeAdmin(admin.ModelAdmin):
    exclude = ("created_by",)
    list_display = ("name","surname")

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        return super(EmployeeAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.created_by :
            return True
        return False
    def has_change_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:
            return True
        return False




class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "product_type","isHomeProduct", "product_code")
    list_filter = ("product_type", "isHomeProduct")

admin.site.register(Market, MarketAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ContactInfo)
admin.site.register(MarketProduct)
