from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import DailyCheckup
from .serializers import DailyCheckupSerializer


@api_view(['POST'])
def save_daily_checkup(request):
    data = {**request.data}
    data = {**data, "date_recorded": datetime.now().date(), "patient": request.user.pk}
    serializer = DailyCheckupSerializer(data=data)
    if serializer.is_valid():
        serializer.save()  # Save the validated data to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_daily_checkups(request, patient_id):
    try:
        # Retrieve daily checkups for a specific patient
        checkups = DailyCheckup.objects.filter(patient__id=patient_id).order_by('-date_recorded')
        # Apply pagination
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(checkups, request)
        serializer = DailyCheckupSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except DailyCheckup.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

