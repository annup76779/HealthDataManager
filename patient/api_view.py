from datetime import datetime, timedelta

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from .models import (
    BloodGlucose, Medication, InsulinUse, BloodPressure,
    PhysicalActivity, StepCount, DietaryIntake, Weight,
    SleepPatterns, MoodAndEmotionalWellBeing, Hydration,
    FootHealthCheck, AssignedToDoctor
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
    permission_classes = [IsAuthenticated]
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
            blood_glucose = BloodGlucose.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            medications = Medication.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            insulin_use = InsulinUse.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            blood_pressure = BloodPressure.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            physical_activity = PhysicalActivity.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            step_count = StepCount.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            dietary_intake = DietaryIntake.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            weight = Weight.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            sleep_patterns = SleepPatterns.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            mood = MoodAndEmotionalWellBeing.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            hydration = Hydration.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
            foot_health_check = FootHealthCheck.objects.filter(patient=request.user, date__range=(start_date, end_date)).order_by('-date')
        else:
            # Collect all data for today (or adjust to fetch data for a different date range if needed)
            blood_glucose = BloodGlucose.objects.filter(patient=request.user).order_by('-date')
            medications = Medication.objects.filter(patient=request.user).order_by('-date')
            insulin_use = InsulinUse.objects.filter(patient=request.user).order_by('-date')
            blood_pressure = BloodPressure.objects.filter(patient=request.user).order_by('-date')
            physical_activity = PhysicalActivity.objects.filter(patient=request.user).order_by('-date')
            step_count = StepCount.objects.filter(patient=request.user).order_by('-date')
            dietary_intake = DietaryIntake.objects.filter(patient=request.user).order_by('-date')
            weight = Weight.objects.filter(patient=request.user).order_by('-date')
            sleep_patterns = SleepPatterns.objects.filter(patient=request.user).order_by('-date')
            mood = MoodAndEmotionalWellBeing.objects.filter(patient=request.user).order_by('-date')
            hydration = Hydration.objects.filter(patient=request.user).order_by('-date')
            foot_health_check = FootHealthCheck.objects.filter(patient=request.user).order_by('-date')
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


class DoctorsDropdown(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search = request.GET.get("search")
        userObjs = User.objects
        if search and search.strip():
            userObjs = userObjs.filter(Q(username__icontains=search.strip()) | Q(first_name__icontains=search.strip()))

        response = [{"id": doc.id, "text": doc.first_name} for doc in userObjs.all()[:30]]
        return Response({"doctors": response})


class ManageDailyLogAccess(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        doctor = request.data.get("doctor")

        start_date = datetime.strptime(start_date, '%Y-%m-%d')

        if end_date:
            print("End Date", end_date)
            end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
        elif start_date:
            end_date = start_date + timedelta(days=1)

        try:
            assigned_data = AssignedToDoctor.objects.get(patient=request.user, doctor__id=doctor)
            assigned_data.from_date = start_date
            assigned_data.to_date = end_date
        except AssignedToDoctor.DoesNotExist:
            try:
                assigned_data = AssignedToDoctor.objects.create(patient=request.user, doctor=User.objects.get(id=doctor), from_date=start_date, to_date=end_date)
            except User.DoesNotExist:
                return Response({
                    "error": "Invalid doctor id"
                }, status=500)
        return Response({
            'assigned_data': {
                "doctor": assigned_data.doctor.first_name,
                "patient": request.user.first_name,
                "from_date": assigned_data.from_date.strftime("%Y-%m-%d"),
                "to_date": assigned_data.to_date.strftime("%Y-%m-%d"),
                "msg": "Assigned daily log to %s from %s to %s" % (assigned_data.doctor.first_name, assigned_data.from_date.strftime("%Y-%m-%d"), assigned_data.to_date.strftime("%Y-%m-%d"))
            }
        })
