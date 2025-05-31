from django.apps import AppConfig
import os

class ImagerieConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "imagerie"

    # def ready(self):
    #     from . import updater
    #     if os.environ.get('RUN_MAIN'):
    #         updater.start()