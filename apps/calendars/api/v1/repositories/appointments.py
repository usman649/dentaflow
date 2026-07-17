from apps.core.exceptions import ObjectNotFoundException
from apps.calendars.models import Appointment


class AppointmentRepository:
    def get_appointments(self):
        appointments = Appointment.objects.all()
        return appointments