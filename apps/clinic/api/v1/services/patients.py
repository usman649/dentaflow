from apps.clinic.api.v1.repositories.patients import PatientRepository
from apps.clinic.api.v1.serializers.patients import (
    PatientListSerializer,
    PatientCreateUpdateSerializer,
    PatientDetailSerializer,
)
from apps.core.services import BaseService
from apps.clinic.api.v1.filters.patients import PatientFilter
from apps.authentication.models import User


class PatientService(BaseService):
    def __init__(self,request):
        super().__init__(request)
        self.db = PatientRepository()

    def get_patients(self,*args,**kwargs):
        unfiltered_patients = self.db.get_patients()
        filtered_patients = PatientFilter(
            data=self.request.query_params,
            queryset=unfiltered_patients,
            request=self.request,
        ).qs

        return self.get_paginated_response(
            filtered_patients,
            PatientListSerializer,
            context={'request': self.request},

        )

    def create_patient(self,*args,**kwargs):
        serializer_class = PatientCreateUpdateSerializer(
            data=self.request.data,context={'request': self.request},
        )
        serializer_class.is_valid(raise_exception=True)
        company = serializer_class.save(role=User.Roles.PATIENT)
        return self.get_response_object(
            company,
            PatientListSerializer,
            context={'request': self.request}
        )

    def get_patient(self,*args,**kwargs):
        patient = self.db.get_patient(user_id=kwargs.get('pk'))
        return self.get_response(
            patient,
            PatientDetailSerializer,
            context={'request': self.request}
        )



