from django import forms
from .models import (
    BloodGlucose, Medication, InsulinUse, BloodPressure,
    PhysicalActivity, StepCount, DietaryIntake, Weight,
    SleepPatterns, MoodAndEmotionalWellBeing, Hydration,
    FootHealthCheck
)


class BloodGlucoseForm(forms.ModelForm):
    class Meta:
        model = BloodGlucose
        fields = ['reading_type', 'glucose_level', 'time_of_reading']
        widgets = {
            'time_of_reading': forms.TimeInput(attrs={'type': 'time'}),
        }


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dose', 'time_taken', 'missed_dose']
        widgets = {
            'time_taken': forms.TimeInput(attrs={'type': 'time'}),
        }


class InsulinUseForm(forms.ModelForm):
    class Meta:
        model = InsulinUse
        fields = ['insulin_type', 'dose_units', 'time_of_administration', 'injection_site']
        widgets = {
            'time_of_administration': forms.TimeInput(attrs={'type': 'time'}),
        }


class BloodPressureForm(forms.ModelForm):
    class Meta:
        model = BloodPressure
        fields = ['systolic', 'diastolic', 'time_of_reading']
        widgets = {
            'time_of_reading': forms.TimeInput(attrs={'type': 'time'}),
        }


class PhysicalActivityForm(forms.ModelForm):
    class Meta:
        model = PhysicalActivity
        fields = ['exercise_type', 'duration', 'intensity', 'time_of_exercise']
        widgets = {
            'time_of_exercise': forms.TimeInput(attrs={'type': 'time'}),
        }


class StepCountForm(forms.ModelForm):
    class Meta:
        model = StepCount
        fields = ['total_steps', 'daily_goal']


class DietaryIntakeForm(forms.ModelForm):
    class Meta:
        model = DietaryIntake
        fields = ['meal', 'carb_intake', 'sugary_foods', 'time_of_meal']
        widgets = {
            'time_of_meal': forms.TimeInput(attrs={'type': 'time'}),
        }


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ['weight']


class SleepPatternsForm(forms.ModelForm):
    class Meta:
        model = SleepPatterns
        fields = ['sleep_duration', 'sleep_quality', 'wake_up_time', 'bedtime']
        widgets = {
            'wake_up_time': forms.TimeInput(attrs={'type': 'time'}),
            'bedtime': forms.TimeInput(attrs={'type': 'time'}),
        }


class MoodAndEmotionalWellBeingForm(forms.ModelForm):
    class Meta:
        model = MoodAndEmotionalWellBeing
        fields = ['mood_rating', 'notable_events']


class HydrationForm(forms.ModelForm):
    class Meta:
        model = Hydration
        fields = ['water_intake', 'dehydration_symptoms']


class FootHealthCheckForm(forms.ModelForm):
    class Meta:
        model = FootHealthCheck
        fields = ['foot_check_completed', 'abnormalities', 'pain_level']
