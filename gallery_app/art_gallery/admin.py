from django.contrib import admin
from .models import *

class ExhibitionAdmin (admin.ModelAdmin):


    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ExhibitionAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


class AuthorAdmin (admin.ModelAdmin):
    exclude = ('user',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(AuthorAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

admin.site.register (Artist)
admin.site.register (Artwork)
admin.site.register (Exhibition)