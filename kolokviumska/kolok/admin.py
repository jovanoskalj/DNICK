from django.contrib import admin
from django import forms
from django.db.models import Count

from .models import Travel, Guide





class GuideAdmin(admin.ModelAdmin):

    exclude = ('user',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
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
        super().save_model(request, obj, form, change)


class TravelAdmin(admin.ModelAdmin):
    exclude = ('guide',)

    def has_add_permission(self, request):
        return Guide.objects.filter(user=request.user).exists()

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return obj and obj.guide.user == request.user

    def save_model(self, request, obj, form, change):
        guide = Guide.objects.filter(user=request.user).first()
        if not guide:
            return

        if not change:
            if Travel.objects.filter(guide=guide).count() >= 5:
                return

        if not change and  Travel.objects.filter(place_name=obj.place_name).exists():
            return


        guide_tours = Travel.objects.filter(guide=guide)
        total_price = sum(tour.price for tour in guide_tours)

        if not change and total_price + obj.price > 50000:
            return

        if change:
            old_obj = Travel.objects.filter(id=obj.id).first()
            if old_obj and total_price + obj.price - old_obj.price > 50000:
                return


        obj.guide = guide
        super().save_model(request, obj, form, change)


admin.site.register(Guide, GuideAdmin)
admin.site.register(Travel, TravelAdmin)
