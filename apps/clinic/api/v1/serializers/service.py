from rest_framework import serializers
from apps.clinic.models import (
    Service,
    Material
)

class ServiceListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    duration_minutes = serializers.IntegerField()
    treatment_type = serializers.CharField()
    is_active = serializers.BooleanField()

class ServiceCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'name',
            'price',
            'duration_minutes',
            'treatment_type',
        ]

class MaterialListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    service = serializers.CharField()
    quantity = serializers.IntegerField()

class MaterialCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = [
            'name',
            'service',
            'quantity',
        ]
