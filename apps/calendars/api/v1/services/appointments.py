from apps.calendars.models import Appointment
from apps.calendars.api.v1.serializers.appointments import (
    AppointmentListSerializer,
    AppointmentCreateUpdateSerializer
)
from apps.calendars.api.v1.repositories.appointments import AppointmentRepository
from apps.core.services import BaseService
from apps.calendars.api.v1.filters.appointments import AppointmentFilter


class AppointmentService(BaseService):
    def __init__(self,request):
        super().__init__(request)
        self.db = AppointmentRepository()

    def get_appointments(self,*args,**kwargs):
        unfiltered_appointments = self.db.get_appointments()
        filtered_appointments = AppointmentFilter(
            data=self.request.query_params,
            queryset=unfiltered_appointments,
            request=self.request,
        ).qs

        return self.get_paginated_response(
            filtered_appointments,
            AppointmentListSerializer,
            context={'request': self.request},
        )

    def create_appointment(self,*args,**kwargs):
        serializer_class= AppointmentCreateUpdateSerializer(
            data=self.request.data,context={'request': self.request}
        )
        serializer_class.is_valid(raise_exception=True)
        appointment = serializer_class.save()
        return self.get_response_object(
            appointment,
            AppointmentListSerializer,
            context={'request': self.request},
        )