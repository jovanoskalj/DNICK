from django.contrib import admin
from .models import *


# Register your models here.
class HospitalDrugsInlines(admin.TabularInline):
    model = HospitalDrugs
    extra = 0


# Додавање и бришење на болници е дозволено само за супер корисници.
class HospitalAdmin(admin.ModelAdmin):
    exclude = ("created_by",)
    inlines = [HospitalDrugsInlines]

    def get_readonly_fields(self, request, obj=None):
        if obj is None or obj.created_by == request.user:
            return []
        return ["name", "address",]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        return super(HospitalAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:
            return True
        return False

class DoctorAdmin (admin.ModelAdmin):
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        return super(DoctorAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:
            return True
        return False

class PatientAdmin (admin.ModelAdmin):
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        return super(PatientAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.created_by == request.user:
            return True
        return False

class DrugAdmin (admin.ModelAdmin):
    list_filter = ("drug_type","prescription_required",)

admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Address)
admin.site.register(Drugs,DrugAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(HospitalDrugs)
