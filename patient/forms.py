from django import forms
from .models import (
    BloodGlucose, Medication, InsulinUse, BloodPressure,
    PhysicalActivity, StepCount, DietaryIntake, Weight,
    SleepPatterns, MoodAndEmotionalWellBeing, Hydration,
    FootHealthCheck
)


class CustomModelForm(forms.ModelForm):
    # Override the save method to add the user before saving
    def save(self, commit=True, user=None, field_value=None):
        if field_value is None:
            field_value = {}
        instance = super().save(commit=False)
        if user:
            instance.patient = user  # Set the user
        if field_value.__len__() > 0:
            for key, value in field_value.items():
                try:
                    setattr(instance, key, value)
                except AttributeError:
                    pass
        if commit:
            instance.save()
        return instance


class BloodGlucoseForm(CustomModelForm):
    class Meta:
        model = BloodGlucose
        fields = ['reading_type', 'glucose_level', 'time_of_reading']
        widgets = {
            'time_of_reading': forms.TimeInput(attrs={'type': 'time'}),
        }


class MedicationForm(CustomModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dose', 'time_taken', 'missed_dose']
        widgets = {
            'time_taken': forms.TimeInput(attrs={'type': 'time'}),
        }


class InsulinUseForm(CustomModelForm):
    class Meta:
        model = InsulinUse
        fields = ['insulin_type', 'dose_units', 'time_of_administration', 'injection_site']
        widgets = {
            'time_of_administration': forms.TimeInput(attrs={'type': 'time'}),
        }


class BloodPressureForm(CustomModelForm):
    class Meta:
        model = BloodPressure
        fields = ['systolic', 'diastolic', 'time_of_reading']
        widgets = {
            'time_of_reading': forms.TimeInput(attrs={'type': 'time'}),
        }


class PhysicalActivityForm(CustomModelForm):
    class Meta:
        model = PhysicalActivity
        fields = ['exercise_type', 'duration', 'intensity', 'time_of_exercise']
        widgets = {
            'time_of_exercise': forms.TimeInput(attrs={'type': 'time'}),
        }


class StepCountForm(CustomModelForm):
    class Meta:
        model = StepCount
        fields = ['total_steps', 'daily_goal']


class DietaryIntakeForm(CustomModelForm):
    class Meta:
        model = DietaryIntake
        fields = ['carb_intake', 'sugary_foods', 'time_of_meal']
        widgets = {
            'time_of_meal': forms.TimeInput(attrs={'type': 'time'}),
        }


class WeightForm(CustomModelForm):
    class Meta:
        model = Weight
        fields = ['weight']


class SleepPatternsForm(CustomModelForm):
    class Meta:
        model = SleepPatterns
        fields = ['sleep_duration', 'sleep_quality', 'wake_up_time', 'bedtime']
        widgets = {
            'wake_up_time': forms.TimeInput(attrs={'type': 'time'}),
            'bedtime': forms.TimeInput(attrs={'type': 'time'}),
        }


class MoodAndEmotionalWellBeingForm(CustomModelForm):
    class Meta:
        model = MoodAndEmotionalWellBeing
        fields = ['mood_rating', 'notable_events']

        labels = {
            'mood_rating': 'Mood Rating (1 lowest / 10 highest)'
        }


class HydrationForm(CustomModelForm):
    class Meta:
        model = Hydration
        fields = ['water_intake', 'dehydration_symptoms']


class FootHealthCheckForm(CustomModelForm):
    class Meta:
        model = FootHealthCheck
        fields = ['foot_check_completed', 'abnormalities', 'pain_level']
