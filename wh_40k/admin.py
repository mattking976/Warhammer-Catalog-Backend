from django.contrib import admin
from .models import wh40k
from .models import Factions

@admin.register(wh40k)
class Wh40kAdmin(admin.ModelAdmin):
    list_display = ('unit_name', 'unit_type', 'codex_page', 'points_cost', 'is_built', 'is_painted', 'faction')
    list_filter = ('unit_type', 'is_built', 'is_painted', 'faction')
    search_fields = ('unit_name',)
    ordering = ('unit_name', 'unit_type', 'points_cost', 'is_built', 'is_painted', 'faction')

@admin.register(Factions)
class FactionsAdmin(admin.ModelAdmin):
    list_display = ('faction_name',)
    search_fields = ('faction_name',)
    ordering = ('faction_name',)
