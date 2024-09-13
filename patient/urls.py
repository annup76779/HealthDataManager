from django.urls import path

from patient.api_view import save_daily_checkup, get_daily_checkups
from patient.views import add_daily_details, get_daily_details

views = [
    path("add_daily_details", add_daily_details, name="daily_details"),
    path("get_daily_details", get_daily_details, name="get_daily_details"),
]

api = [
    path('daily_checkup', save_daily_checkup, name='save_daily_checkup'),
    path('daily_checkup/<int:patient_id>/', get_daily_checkups, name='get_daily_checkups'),
]

urlpatterns = views + api

