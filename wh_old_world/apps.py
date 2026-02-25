from django.apps import AppConfig


class OldWorldConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wh_old_world'

class FactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wh_old_world.factions'
