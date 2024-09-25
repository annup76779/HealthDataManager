from django.urls import path

from doctor.api_view import LogsData, PatientsDropdown
from doctor.views import home

urlpatterns = [
    path("home", home, name="doctor-home"),
    path("logs", LogsData.as_view(), name="doctors-provided-logs"),
    path("patients_dropdown", PatientsDropdown.as_view(), name="patient-dropdown")
]
