from django.apps import AppConfig


class PatuvanjaappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patuvanjaApp'

    def ready(self):
        from . import signals