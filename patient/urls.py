from django.urls import path, include
from rest_framework.routers import DefaultRouter

from patient.api_view import *
from patient.views import add_daily_details, get_daily_details, health_data_view

views = [
    path("add_daily_details", add_daily_details, name="daily_details"),
    path("get_daily_details", get_daily_details, name="get_daily_details"),
]


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'blood-glucose', BloodGlucoseViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'insulin-use', InsulinUseViewSet)
router.register(r'blood-pressure', BloodPressureViewSet)
router.register(r'physical-activity', PhysicalActivityViewSet)
router.register(r'step-count', StepCountViewSet)
router.register(r'dietary-intake', DietaryIntakeViewSet)
router.register(r'weight', WeightViewSet)
router.register(r'sleep-patterns', SleepPatternsViewSet)
router.register(r'mood-emotional-wellbeing', MoodAndEmotionalWellBeingViewSet)
router.register(r'hydration', HydrationViewSet)
router.register(r'foot-health-check', FootHealthCheckViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('health-data/', health_data_view, name='health_data_view'),
    path("get-health-data", DailyHealthDataView.as_view(), name="get_health_data"),
    path("manage-data", ManageDailyLogAccess.as_view(), name="manage_data_access"),
    path("doctors-dropdown", DoctorsDropdown.as_view(), name="doctors_dropdown"),
]

urlpatterns.extend(views)

