from django.contrib import admin
from .models import ForceOrg

@admin.register(ForceOrg)
class ForceOrgAdmin(admin.ModelAdmin):
    list_display = ('unit_name', 'unit_type', 'codex_page', 'points_cost', 'is_built', 'is_painted')
    list_filter = ('unit_type', 'is_built', 'is_painted')
    search_fields = ('unit_name',)
    ordering = ('unit_name', 'unit_type', 'points_cost', 'is_built', 'is_painted')
