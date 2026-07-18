from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg  import openapi
from rest_framework.views import APIView
from apps.clinic.api.v1.serializers.service import (
    ServiceListSerializer,
    MaterialListSerializer,
    ServiceCreateUpdateSerializer,
    MaterialCreateUpdateSerializer
)
from apps.clinic.api.v1.services.service import ServiceService

class ServiceCreateListView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=ServiceCreateUpdateSerializer,
        responses={200: ServiceListSerializer},
        tags=['Service'],
        operation_description='Service Create',
    )
    def post(self,request,*args,**kwargs):
        return ServiceService(request=request).create_service(*args,**kwargs)

    @swagger_auto_schema(
        responses={200: ServiceListSerializer},
        tags=['Service'],
        operation_description='Service List',
        manual_parameters=[
            openapi.Parameter(
                name='treatment_type_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='Treatment Type ID',
            )
        ]
    )
    def get(self,request,*args,**kwargs):
        return ServiceService(request=request).get_services(*args,**kwargs)


class ServiceDetailUpdateDeleteView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        request_body=ServiceCreateUpdateSerializer,
        responses={200: ServiceListSerializer},
        tags=['Service'],
        operation_description='Service Update',
    )
    def patch(self,request,*args,**kwargs):
        return ServiceService(request=request).update_service(*args,**kwargs)

    @swagger_auto_schema(
        tags=['Service'],
        operation_description='Service Delete',
    )
    def delete(self,request,*args,**kwargs):
        return ServiceService(request=request).delete_service(*args,**kwargs)


