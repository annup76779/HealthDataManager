from rest_framework import serializers
from .models import DailyCheckup


class DailyCheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCheckup
        fields = '__all__'  # Serialize all fields of the DailyCheckup model

    # Optionally, you can add custom validation for specific fields
    def validate_blood_sugar_morning(self, value):
        if value < 0:
            raise serializers.ValidationError("Blood sugar cannot be negative")
        return value
