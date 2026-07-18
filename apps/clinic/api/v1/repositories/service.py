from apps.core.exceptions import ObjectNotFoundException
from apps.clinic.models import (
    Service,
)

class ServiceRepository:
    def get_services(self):
        services = Service.objects.all()
        return services

    def get_service(self,service_id):
        service = Service.objects.filter(id=service_id).first()
        if not service:
            raise ObjectNotFoundException(
                message='Service does not exist',
                message_key='service_does_not_exist',
            )
        return service



