from rest_framework import serializers
from .models import StrainOperation, StrainStock

class StrainStockSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        if StrainStock.objects.filter(strain_name=data['strain_name'], user=data['user']).exists():
            raise serializers.ValidationError("Can't have two strains of the same name")
        return data

    class Meta:
        model = StrainStock
        fields = ["id", "strain_name", "quantity", "user", "created_at"]

class StrainOperationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = StrainOperation
        fields = ["id", "strain", "user", "quantity", "created_at"]

