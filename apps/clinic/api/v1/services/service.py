from apps.clinic.api.v1.repositories.service import ServiceRepository
from apps.clinic.api.v1.serializers.service import (
    ServiceListSerializer,
    MaterialListSerializer,
    ServiceCreateUpdateSerializer,
    MaterialCreateUpdateSerializer
)
from apps.core.services import BaseService
from rest_framework import status
from apps.clinic.api.v1.filters.service import ServiceFilter


class ServiceService(BaseService):
    def __init__(self,request):
        super().__init__(request)
        self.db = ServiceRepository()

    def create_service(self,*args,**kwargs):
        serializer_class = ServiceCreateUpdateSerializer(
            data=self.request.data,context={'request': self.request},
        )
        serializer_class.is_valid(raise_exception=True)
        service = serializer_class.save()
        return self.get_response_object(
            service,
            ServiceListSerializer,
            context={'request': self.request},
        )

    def update_service(self, *args, **kwargs):
        service = self.db.get_service(service_id=kwargs.get('pk'))
        serializer_class = ServiceCreateUpdateSerializer(
            instance=service,
            data=self.request.data,
            partial=True,
            context={'request': self.request}
        )
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return self.get_response_object(
            obj=service,
            response_serializer_class=ServiceListSerializer,
            context={'request': self.request}
        )

    def delete_service(self, *args, **kwargs):
        service = self.db.get_service(service_id=kwargs.get('pk'))
        service.delete()
        return self.get_response_object(
            context={'request': self.request},
            status_code=status.HTTP_204_NO_CONTENT,
        )

    def get_services(self,*args,**kwargs):
        unfiltered_services = self.db.get_services()
        filtered_services = ServiceFilter(
            data=self.request.query_params,
            queryset=unfiltered_services,
            request=self.request,
        ).qs

        return self.get_paginated_response(
            filtered_services,
            ServiceListSerializer,
            context={'request': self.request},

        )





