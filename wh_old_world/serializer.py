from rest_framework import serializers
from .models import OldWorld
from .models import OldWorldFactions

class OldWorldSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    unit_name = serializers.CharField()
    unit_type = serializers.CharField()
    forces_of_evil_page = serializers.IntegerField()
    arcane_journal_page = serializers.IntegerField()
    points_cost = serializers.IntegerField()
    is_built = serializers.BooleanField()
    is_painted = serializers.BooleanField()
    faction = serializers.CharField(source='faction.faction_name')

    class Meta:
        model = OldWorld
        fields = (
            'id',
            'unit_name',
            'unit_type',
            'forces_of_evil_page',
            'arcane_journal_page',
            'points_cost',
            'is_built',
            'is_painted',
            'faction',
        )

class OldWorldFactionsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    faction_name = serializers.CharField()

    class Meta:
        model = OldWorldFactions
        fields = (
            'id',
            'faction_name',
        )
