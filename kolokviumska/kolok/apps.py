from django.apps import AppConfig


class KolokConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kolok'
    def ready(self):
        from . import signals
