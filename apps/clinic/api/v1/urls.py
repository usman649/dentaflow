from django.urls import path
from apps.clinic.api.v1 import views

urlpatterns = [
    path(
        'patients/',
        views.PatientCreateListView.as_view(),
        name='patients-list',
    ),
    path(
        'patients/<int:pk>/',
        views.PatientDetailUpdateDeleteView.as_view(),
        name='patient-detail'
    ),
    path(
        'doctors/',
        views.DoctorCreateListView.as_view(),
        name='doctors-create-list',
    ),
    path(
        'doctors/<int:pk>/',
        views.DoctorDetailUpdateDeleteView.as_view(),
        name='doctor-detail-update-delete',
    ),
    path(
        'treatments/',
        views.TreatmentCreateListView.as_view(),
        name='treatments-create-list',
    ),
    path(
        'treatment-types/',
        views.TreatmentTypeListView.as_view(),
        name='treatment-type-list',
    ),
    path(
        'galleries/',
        views.GalleryCreateView.as_view(),
        name='gallery-create',
    ),
    path(
        'services/',
        views.ServiceCreateListView.as_view(),
        name='service-create-list',
    ),
    path(
        'services/<int:pk>/',
        views.ServiceDetailUpdateDeleteView.as_view(),
        name='service-detail-update',
    )



]