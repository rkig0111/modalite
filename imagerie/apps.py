from django.apps import AppConfig
import os

class ImagerieConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "imagerie"

    def ready(self):
        from . import updater
        updater.start()