from rest_framework import serializers
from .models import wh40k
from .models import Factions


class ForceOrgSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    unit_name = serializers.CharField()
    unit_type = serializers.CharField()
    codex_page = serializers.IntegerField()
    points_cost = serializers.IntegerField()
    is_built = serializers.BooleanField()
    is_painted = serializers.BooleanField()
    faction = serializers.CharField(source='faction.faction_name')

    class Meta:
        model = wh40k
        fields = (
            'id',
            'unit_name',
            'unit_type',
            'codex_page',
            'points_cost',
            'is_built',
            'is_painted',
            'faction',
        )

class FactionsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    faction_name = serializers.CharField()

    class Meta:
        model = Factions
        fields = (
            'id',
            'faction_name',
        )