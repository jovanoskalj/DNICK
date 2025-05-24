from django.apps import AppConfig


class RealestateappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'realEstateApp'

    def ready(self):
        from .import signals
