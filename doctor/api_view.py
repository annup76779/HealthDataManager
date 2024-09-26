from copy import copy
from datetime import datetime, timedelta

from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from patient.api_view import StandardResultsSetPagination
from patient.models import AssignedToDoctor, BloodGlucose, Medication, InsulinUse, BloodPressure, PhysicalActivity, \
    StepCount, DietaryIntake, Weight, SleepPatterns, MoodAndEmotionalWellBeing, Hydration, FootHealthCheck
from patient.serializers import *


class LogsData(APIView):
    permission_classes = [IsAuthenticated]

    def object_serialize(self, obj, serializer):
        return serializer(instance=obj).data

    def post(self, request):
        patient = request.data.get("patient")

        try:
            assigned_logs: AssignedToDoctor = AssignedToDoctor.objects.get(patient__id=patient, doctor=request.user)
        except AssignedToDoctor.DoesNotExist:
            return Response({"error": "Invalid request"}, status=400)
        class_serializer_array = [
            [BloodGlucose, BloodGlucoseSerializer, 'blood_glucose'],
            [Medication, MedicationSerializer, 'medications'],
            [InsulinUse, InsulinUseSerializer, 'insulin_use'],
            [BloodPressure, BloodPressureSerializer, 'blood_pressure'],
            [PhysicalActivity, PhysicalActivitySerializer, 'physical_activity'],
            [StepCount, StepCountSerializer, 'step_count'],
            [DietaryIntake, DietaryIntakeSerializer, 'dietary_intake'],
            [Weight, WeightSerializer, 'weight'],
            [SleepPatterns, SleepPatternsSerializer, 'sleep_patterns'],
            [MoodAndEmotionalWellBeing, MoodAndEmotionalWellBeingSerializer, 'mood'],
            [Hydration, HydrationSerializer, 'hydration'],
            [FootHealthCheck, FootHealthCheckSerializer, 'foot_health_check']
        ]

        logs = {}

        block_log = {
            'blood_glucose': None,
            'medications': None,
            'insulin_use': None,
            'blood_pressure': None,
            'physical_activity': None,
            'step_count': None,
            'dietary_intake': None,
            'weight': None,
            'sleep_patterns': None,
            'mood': None,
            'hydration': None,
            'foot_health_check': None,
        }

        pagination = StandardResultsSetPagination()

        for class_name_srlz in class_serializer_array:
            class_name, srlz, key = class_name_srlz
            if key == 'dietary_intake':
                pagination.page_size = pagination.page_size * 4
            else:
                pagination.page_size = 10
            objs = pagination.paginate_queryset(class_name.objects.filter(patient=assigned_logs.patient, date__range=(assigned_logs.from_date, assigned_logs.to_date + timedelta(days=1))), request)
            for obj in objs:
                date_key = obj.date.strftime("%Y-%m-%d")
                if obj.date.strftime("%Y-%m-%d") in logs.keys():
                    if key == "dietary_intake":
                        if isinstance(logs[date_key].get(key), (list, tuple)):
                            logs[date_key][key].append(self.object_serialize(obj, srlz))
                        else:
                            logs[date_key][key] = [self.object_serialize(obj, srlz)]
                    else:
                        logs[date_key][key] = self.object_serialize(obj, srlz)
                else:
                    logs[date_key] = copy(block_log)
                    logs[date_key][key] = self.object_serialize(obj, srlz) if key != "dietary_intake" else [self.object_serialize(obj, srlz)]

        count = BloodGlucose.objects.filter(patient=assigned_logs.patient, date__range=(assigned_logs.from_date, assigned_logs.to_date + timedelta(days=1))).count()
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1
        return Response({
            'count': count,
            'next': request.POST.get("page", 1) + 1 if page * pagination.page_size < count else False,
            'previous': page - 1,
            'results': logs
        })


class PatientsDropdown(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search = request.GET.get("search")
        logObjs = AssignedToDoctor.objects.filter(doctor=request.user)
        if search and search.strip():
            logObjs = logObjs.filter(Q(patient__username__icontains=search.strip()) | Q(patient__first_name__icontains=search.strip()))

        response = [{"id": log.patient.id, "text": log.patient.first_name} for log in logObjs.all()[:30]]
        return Response({"patients": response})

