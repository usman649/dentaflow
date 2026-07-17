from django.urls import path
from apps.calendars.api.v1 import views


urlpatterns = [
    path(
        'appointments/',
        views.AppointmentCreateListView.as_view(),
        name='appointments'
    ),


]