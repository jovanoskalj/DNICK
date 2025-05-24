from xmlrpc.client import DateTime

from django.contrib import admin
from .models import *
from datetime import date, datetime


class RealEstateAgentInline(admin.TabularInline):
    model = RealEstateAgent
    extra = 0


class RealEstateCharacteristicsInline(admin.TabularInline):
    model = RealEstateCharacteristics
    extra = 0


class RealEstateAdmin(admin.ModelAdmin):
    inlines = [RealEstateAgentInline, RealEstateCharacteristicsInline,]
    list_display = ('name', 'area', 'description',)

    def has_add_permission(self, request):
        #Огласи за продажба може да бидат додадени само од агенти
        return Agent.objects.filter(user=request.user).exists()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # по автоматизам агентот кој додава оглас е еден од задолжените за продажба на таа недвижност
        if not change:
            agent = Agent.objects.filter(user=request.user).first()  # ovoa da se napise u roadmap
            RealEstateAgent.objects.create(real_estate=obj, agent=agent)  # ovoa da se napise u roadmap

    def has_delete_permission(self, request, obj=None):
        # Еден оглас може да биде избришан само ако нема
        # додадено ниту една карактеристика која го опишува
        return not RealEstateCharacteristics.objects.filter(real_estate=obj).exists()

    def has_change_permission(self, request, obj=None):
        return obj and RealEstateAgent.objects.filter(real_estate=obj, agent__user=request.user).exists()

    def has_view_permission(self, request, obj=None):
        # Oстанатите агенги може само да ги гледаат тие огласи
        return True

    def get_queryset(self, request):
        # На супер-корисниците во Админ панелот им се
        # прикажуваат само огласите кои се објавени на денешен датум
        if request.user.is_superuser:
            return RealEstate.objects.filter(date=datetime.now().date())
        return RealEstate.objects.all()


class AgentAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name', 'surname',)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        obj.user = request.user

        super().save_model(request, obj, form, change)


class CharacteristicsAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Agent,AgentAdmin)
admin.site.register(RealEstate,RealEstateAdmin)
admin.site.register(Characteristics,CharacteristicsAdmin)
