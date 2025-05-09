from django.contrib import admin
from .models import *


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def get_queryset(self, request):
        return Event.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if request.user == User.is_superuser:
            obj.user = request.user
            return super(EventAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False



admin.site.register(Band)
admin.site.register(Event)
admin.site.register(BandEvent)
