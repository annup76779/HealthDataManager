from datetime import datetime, timedelta

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from .models import (
    BloodGlucose, Medication, InsulinUse, BloodPressure,
    PhysicalActivity, StepCount, DietaryIntake, Weight,
    SleepPatterns, MoodAndEmotionalWellBeing, Hydration,
    FootHealthCheck
)
from .serializers import (
    BloodGlucoseSerializer, MedicationSerializer, InsulinUseSerializer, BloodPressureSerializer,
    PhysicalActivitySerializer, StepCountSerializer, DietaryIntakeSerializer, WeightSerializer,
    SleepPatternsSerializer, MoodAndEmotionalWellBeingSerializer, HydrationSerializer,
    FootHealthCheckSerializer, DailyHealthDataSerializer
)

from django.utils import timezone


# Custom pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Number of records per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Optional, to limit the number of records


# Blood Glucose ViewSet
class BloodGlucoseViewSet(viewsets.ModelViewSet):
    queryset = BloodGlucose.objects.all()
    serializer_class = BloodGlucoseSerializer
    pagination_class = StandardResultsSetPagination


# Medication ViewSet
class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    pagination_class = StandardResultsSetPagination


# Insulin Use ViewSet
class InsulinUseViewSet(viewsets.ModelViewSet):
    queryset = InsulinUse.objects.all()
    serializer_class = InsulinUseSerializer
    pagination_class = StandardResultsSetPagination


# Blood Pressure ViewSet
class BloodPressureViewSet(viewsets.ModelViewSet):
    queryset = BloodPressure.objects.all()
    serializer_class = BloodPressureSerializer
    pagination_class = StandardResultsSetPagination


# Physical Activity ViewSet
class PhysicalActivityViewSet(viewsets.ModelViewSet):
    queryset = PhysicalActivity.objects.all()
    serializer_class = PhysicalActivitySerializer
    pagination_class = StandardResultsSetPagination


# Step Count ViewSet
class StepCountViewSet(viewsets.ModelViewSet):
    queryset = StepCount.objects.all()
    serializer_class = StepCountSerializer
    pagination_class = StandardResultsSetPagination


# Dietary Intake ViewSet
class DietaryIntakeViewSet(viewsets.ModelViewSet):
    queryset = DietaryIntake.objects.all()
    serializer_class = DietaryIntakeSerializer
    pagination_class = StandardResultsSetPagination


# Weight ViewSet
class WeightViewSet(viewsets.ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    pagination_class = StandardResultsSetPagination


# Sleep Patterns ViewSet
class SleepPatternsViewSet(viewsets.ModelViewSet):
    queryset = SleepPatterns.objects.all()
    serializer_class = SleepPatternsSerializer
    pagination_class = StandardResultsSetPagination


# Mood and Emotional Well-being ViewSet
class MoodAndEmotionalWellBeingViewSet(viewsets.ModelViewSet):
    queryset = MoodAndEmotionalWellBeing.objects.all()
    serializer_class = MoodAndEmotionalWellBeingSerializer
    pagination_class = StandardResultsSetPagination


# Hydration ViewSet
class HydrationViewSet(viewsets.ModelViewSet):
    queryset = Hydration.objects.all()
    serializer_class = HydrationSerializer
    pagination_class = StandardResultsSetPagination


# Foot Health Check ViewSet
class FootHealthCheckViewSet(viewsets.ModelViewSet):
    queryset = FootHealthCheck.objects.all()
    serializer_class = FootHealthCheckSerializer
    pagination_class = StandardResultsSetPagination


class DailyHealthDataView(APIView):
    def get(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')

        if end_date:
            print("End Date", end_date)
            end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
        elif start_date:
            end_date = start_date + timedelta(days=1)

        pagination = StandardResultsSetPagination()

        if start_date and end_date:
            # Collect all data for today (or adjust to fetch data for a different date range if needed)
            blood_glucose = BloodGlucose.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            medications = Medication.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            insulin_use = InsulinUse.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            blood_pressure = BloodPressure.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            physical_activity = PhysicalActivity.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            step_count = StepCount.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            dietary_intake = DietaryIntake.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            weight = Weight.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            sleep_patterns = SleepPatterns.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            mood = MoodAndEmotionalWellBeing.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            hydration = Hydration.objects.filter(date__range=(start_date, end_date)).order_by('-date')
            foot_health_check = FootHealthCheck.objects.filter(date__range=(start_date, end_date)).order_by('-date')
        else:
            # Collect all data for today (or adjust to fetch data for a different date range if needed)
            blood_glucose = BloodGlucose.objects.order_by('-date')
            medications = Medication.objects.order_by('-date')
            insulin_use = InsulinUse.objects.order_by('-date')
            blood_pressure = BloodPressure.objects.order_by('-date')
            physical_activity = PhysicalActivity.objects.order_by('-date')
            step_count = StepCount.objects.order_by('-date')
            dietary_intake = DietaryIntake.objects.order_by('-date')
            weight = Weight.objects.order_by('-date')
            sleep_patterns = SleepPatterns.objects.order_by('-date')
            mood = MoodAndEmotionalWellBeing.objects.order_by('-date')
            hydration = Hydration.objects.order_by('-date')
            foot_health_check = FootHealthCheck.objects.order_by('-date')
        # Combine all the data into one response
        combined_data = {
            'blood_glucose': blood_glucose,
            'medications': medications,
            'insulin_use': insulin_use,
            'blood_pressure': blood_pressure,
            'physical_activity': physical_activity,
            'step_count': step_count,
            'dietary_intake': dietary_intake,
            'weight': weight,
            'sleep_patterns': sleep_patterns,
            'mood': mood,
            'hydration': hydration,
            'foot_health_check': foot_health_check,
        }

        # Serialize the combined data
        serializer = DailyHealthDataSerializer(combined_data)

        # Apply pagination to the serialized data
        paginated_data = pagination.paginate_queryset([serializer.data], request)
        return pagination.get_paginated_response(paginated_data)
