from rest_framework import serializers
from .models import (
    BloodGlucose, Medication, InsulinUse, BloodPressure,
    PhysicalActivity, StepCount, DietaryIntake, Weight,
    SleepPatterns, MoodAndEmotionalWellBeing, Hydration,
    FootHealthCheck
)


class BloodGlucoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodGlucose
        fields = '__all__'


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class InsulinUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsulinUse
        fields = '__all__'


class BloodPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPressure
        fields = "__all__"


class PhysicalActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalActivity
        fields = '__all__'


class StepCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepCount
        fields = '__all__'


class DietaryIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryIntake
        fields = '__all__'


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'


class SleepPatternsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepPatterns
        fields = "__all__"


class MoodAndEmotionalWellBeingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodAndEmotionalWellBeing
        fields = '__all__'


class HydrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hydration
        fields = '__all__'


class FootHealthCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootHealthCheck
        fields = '__all__'


class DailyHealthDataSerializer(serializers.Serializer):
    blood_glucose = BloodGlucoseSerializer(many=True, required=True)
    medications = MedicationSerializer(many=True, required=True)
    insulin_use = InsulinUseSerializer(many=True, required=True)
    blood_pressure = BloodPressureSerializer(many=True, required=True)
    physical_activity = PhysicalActivitySerializer(many=True, required=True)
    step_count = StepCountSerializer(many=True, required=True)
    dietary_intake = DietaryIntakeSerializer(many=True, required=True)
    weight = WeightSerializer(many=True, required=True)
    sleep_patterns = SleepPatternsSerializer(many=True, required=True)
    mood = MoodAndEmotionalWellBeingSerializer(many=True, required=True)
    hydration = HydrationSerializer(many=True, required=True)
    foot_health_check = FootHealthCheckSerializer(many=True, required=True)
