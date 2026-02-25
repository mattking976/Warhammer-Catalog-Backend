from django.contrib import admin
from .models import OldWorld
from .models import OldWorldFactions

@admin.register(OldWorld)
class OldWorldAdmin(admin.ModelAdmin):
    list_display = ('unit_name', 'unit_type', 'forces_of_evil_page', 'arcane_journal_page', 'points_cost', 'is_built', 'is_painted', 'faction')
    list_filter = ('unit_type', 'is_built', 'is_painted', 'faction')
    search_fields = ('unit_name',)
    ordering = ('unit_name', 'unit_type', 'points_cost', 'is_built', 'is_painted', 'faction')

@admin.register(OldWorldFactions)
class OldWorldFactionsAdmin(admin.ModelAdmin):
    list_display = ('faction_name',)
    search_fields = ('faction_name',)
    ordering = ('faction_name',)
