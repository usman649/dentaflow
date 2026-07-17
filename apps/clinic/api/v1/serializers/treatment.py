from rest_framework import serializers
from apps.clinic.models import Treatment

class TreatmentListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    patient = serializers.CharField()
    doctor = serializers.CharField()
    treatment_type = serializers.CharField()
    total_treatment_cost = serializers.IntegerField()
    total_paid = serializers.IntegerField()
    visit_number = serializers.IntegerField()
    tooth_number = serializers.IntegerField()
    start_date = serializers.DateField()
    notes = serializers.CharField()

class TreatmentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = [
            'patient',
            'doctor',
            'treatment_type',
            'total_treatment_cost',
            'total_paid',
            'visit_number',
            'tooth_number',
            'start_date',
            'notes',
        ]

class TreatmentTypeListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
