import django_filters
from apps.clinic.models import Service

class ServiceFilter(django_filters.FilterSet):
    treatment_type_id = django_filters.NumberFilter(
        field_name='treatment_type_id',
    )

    class Meta:
        model = Service
        fields = ['treatment_type_id']