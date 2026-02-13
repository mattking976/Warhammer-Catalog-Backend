from rest_framework import serializers
from .models import ForceOrg

class ForceOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForceOrg
        fields = '__all__'