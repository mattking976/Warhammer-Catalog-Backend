from django.apps import AppConfig


class Wh40kConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wh_40k'

class FactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wh_40k.factions'
