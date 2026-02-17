from rest_framework import serializers
from .models import ForceOrg


class ForceOrgSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    unit_name = serializers.CharField()
    unit_type = serializers.CharField()
    codex_page = serializers.IntegerField()
    points_cost = serializers.IntegerField()
    is_built = serializers.BooleanField()
    is_painted = serializers.BooleanField()

    class Meta:
        model = ForceOrg
        fields = (
            'id',
            'unit_name',
            'unit_type',
            'codex_page',
            'points_cost',
            'is_built',
            'is_painted',
        )