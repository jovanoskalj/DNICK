from django.contrib import admin
from django.db.models import Count

from .models import *


class GuideAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(GuideAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs.annotate(travel_count=Count('travel')).filter(travel_count__lt=3)
        return qs

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return obj and request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return obj and request.user.is_superuser

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(GuideAdmin, self).save_model(request, obj, form, change)


class TravelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return Guide.objects.filter(user=request.user).first()

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def save_model(self, request, obj, form, change):
        # guide = obj.guide.user
        if not change:

            if Travel.objects.filter(guide=obj.guide.user).count() >= 5:
                return
        if Travel.objects.filter(destination=obj.destination).exists():
            return
        guide_tours = Travel.objects.filter(guide=obj.guide.user).all()

        sum = 0
        for tour in guide_tours:
            sum += tour.price
        old_obj_price = guide_tours.filter(id=obj.id).first()
        if not change and sum + obj.price > 50000:
            return
        if change and sum + obj.price - old_obj_price > 50000:
            return

        super(TravelAdmin, self).save_model(request, obj, form, change)


admin.site.register(Travel, TravelAdmin)
admin.site.register(Guide, GuideAdmin)
