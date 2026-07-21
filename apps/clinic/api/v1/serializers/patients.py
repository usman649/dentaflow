from rest_framework import serializers
from apps.authentication.models import User
from apps.clinic.api.v1.serializers.galleries import GalleryListSerializer
from datetime import datetime
from apps.clinic.api.v1.serializers.treatment import TreatmentTypeListSerializer

class PatientListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    appointment_date = serializers.SerializerMethodField()
    treatment_type = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    doctor = serializers.CharField()
    remaining = serializers.SerializerMethodField()
    birth_date = serializers.DateField()
    address = serializers.CharField()
    office = serializers.CharField()


    def get_appointment_date(self, obj):
        latest_appointment = obj.patient_appointments.order_by('-date', '-time').first()
        if latest_appointment:
            date_str = latest_appointment.date.strftime('%d.%m.%Y')
            time_str = latest_appointment.time.strftime('%H:%M')
            return f"{date_str} {time_str}"
        return None

    def get_status(self, obj):
        latest_appointment = obj.patient_appointments.order_by('-date', '-time').first()
        if latest_appointment:
            return latest_appointment.status
        return None

    def get_treatment_type(self, obj):
        treatment = obj.patient_treatments.first()
        if treatment and treatment.treatment_type:
            return treatment.treatment_type.name
        return None

    def get_remaining(self, obj):
        treatment = obj.patient_treatments.first()
        if treatment:
            return treatment.total_treatment_cost - treatment.total_paid
        return None






class PatientCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'full_name',
            'phone_number',
            'doctor',
            'birth_date',
            'address',
            'office',

        ]

class PatientDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    doctor = serializers.CharField()
    image = serializers.ImageField()
    age = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    total_treatment_cost = serializers.SerializerMethodField()
    total_paid = serializers.SerializerMethodField()
    remaining = serializers.SerializerMethodField()
    visit_number = serializers.SerializerMethodField()

    treatment_type = serializers.SerializerMethodField()
    gallery = GalleryListSerializer(many=True,read_only=True)



    def get_age(self,obj):
        if obj.birth_date:
            return datetime.now().year - obj.birth_date.year
        return None

    def get_status(self, obj):
        latest_appointment = obj.patient_appointments.order_by('-date', '-time').first()
        if latest_appointment:
            return latest_appointment.status
        return None

    def get_treatment_type(self, obj):
        treatments = obj.patient_treatments.select_related('treatment_type').all()

        result = []
        for treatment in treatments:
            if treatment.treatment_type:
                result.append({
                    "id": treatment.treatment_type.id,
                    "name": treatment.treatment_type.name,
                    "tooth_number": treatment.tooth_number
                })

        return result

    def get_total_treatment_cost(self, obj):
        treatment = obj.patient_treatments.first()
        if treatment and treatment.total_treatment_cost:
            return treatment.total_treatment_cost
        return 0

    def get_total_paid(self, obj):
        treatment = obj.patient_treatments.first()
        if treatment and treatment.total_paid:
            return treatment.total_paid
        return 0

    def get_remaining(self, obj):
        treatment = obj.patient_treatments.first()
        if treatment:
            return treatment.total_treatment_cost - treatment.total_paid
        return 0

    def get_visit_number(self, obj):
        treatment = obj.patient_treatments.first()
        if treatment and treatment.visit_number:
            return treatment.visit_number
        return 0





