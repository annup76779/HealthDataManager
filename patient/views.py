from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import (
    BloodGlucoseForm, MedicationForm, InsulinUseForm, BloodPressureForm,
    PhysicalActivityForm, StepCountForm, DietaryIntakeForm, WeightForm,
    SleepPatternsForm, MoodAndEmotionalWellBeingForm, HydrationForm, FootHealthCheckForm
)
from .models import (
    BloodGlucose, Medication, InsulinUse, BloodPressure, PhysicalActivity, StepCount, DietaryIntake,
    Weight, SleepPatterns, MoodAndEmotionalWellBeing, Hydration, FootHealthCheck
)
from django.utils import timezone
from django.contrib import messages


# Create your views here.
@login_required
def add_daily_details(request):
    return render(request, "patient/add_daily_details.html")


@login_required
def get_daily_details(request):
    today = datetime.today().strftime("%Y-%m-%d")
    return render(request, "patient/history.html", {"today": today})


@login_required
def health_data_view(request):
    today = timezone.localtime().date()

    # Check if data exists for today, otherwise create empty instances
    blood_glucose = BloodGlucose.objects.filter(date=today).last()
    medication = Medication.objects.filter(date=today).last()
    insulin_use = InsulinUse.objects.filter(date=today).last()
    blood_pressure = BloodPressure.objects.filter(date=today).last()
    physical_activity = PhysicalActivity.objects.filter(date=today).last()
    step_count = StepCount.objects.filter(date=today).last()
    dietary_intake_breakfast = DietaryIntake.objects.filter(date=today, meal=DietaryIntake.BREAKFAST).last()
    dietary_intake_lunch = DietaryIntake.objects.filter(date=today, meal=DietaryIntake.LUNCH).last()
    dietary_intake_snacks = DietaryIntake.objects.filter(date=today, meal=DietaryIntake.SNACKS).last()
    dietary_intake_dinner = DietaryIntake.objects.filter(date=today, meal=DietaryIntake.DINNER).last()
    weight = Weight.objects.filter(date=today).last()
    sleep_patterns = SleepPatterns.objects.filter(date=today).last()
    mood = MoodAndEmotionalWellBeing.objects.filter(date=today).last()
    hydration = Hydration.objects.filter(date=today).last()
    foot_health = FootHealthCheck.objects.filter(date=today).last()

    # Create forms prefilled with existing data if available
    if request.method == 'POST':
        blood_glucose_form = BloodGlucoseForm(request.POST, instance=blood_glucose)
        medication_form = MedicationForm(request.POST, instance=medication)
        insulin_use_form = InsulinUseForm(request.POST, instance=insulin_use)
        blood_pressure_form = BloodPressureForm(request.POST, instance=blood_pressure)
        physical_activity_form = PhysicalActivityForm(request.POST, instance=physical_activity)
        step_count_form = StepCountForm(request.POST, instance=step_count)
        dietary_intake_breakfast_form = DietaryIntakeForm(request.POST, instance=dietary_intake_breakfast, prefix="breakfast")
        dietary_intake_lunch_form = DietaryIntakeForm(request.POST, instance=dietary_intake_lunch, prefix="lunch")
        dietary_intake_snacks_form = DietaryIntakeForm(request.POST, instance=dietary_intake_snacks, prefix="snacks")
        dietary_intake_dinner_form = DietaryIntakeForm(request.POST, instance=dietary_intake_dinner, prefix="dinner")
        weight_form = WeightForm(request.POST, instance=weight)
        sleep_patterns_form = SleepPatternsForm(request.POST, instance=sleep_patterns)
        mood_form = MoodAndEmotionalWellBeingForm(request.POST, instance=mood)
        hydration_form = HydrationForm(request.POST, instance=hydration)
        foot_health_form = FootHealthCheckForm(request.POST, instance=foot_health)

        if all([blood_glucose_form.is_valid(), medication_form.is_valid(), insulin_use_form.is_valid(),
                blood_pressure_form.is_valid(), physical_activity_form.is_valid(), step_count_form.is_valid(),
                dietary_intake_breakfast_form.is_valid(), dietary_intake_lunch_form.is_valid(),
                dietary_intake_snacks_form.is_valid(), dietary_intake_dinner_form.is_valid(), weight_form.is_valid(),
                sleep_patterns_form.is_valid(), mood_form.is_valid(), hydration_form.is_valid(), foot_health_form.is_valid()]):
            blood_glucose_form.save(user=request.user)
            medication_form.save(user=request.user)
            insulin_use_form.save(user=request.user)
            blood_pressure_form.save(user=request.user)
            physical_activity_form.save(user=request.user)
            step_count_form.save(user=request.user)
            dietary_intake_breakfast_form.save(user=request.user, field_value={"meal": DietaryIntake.BREAKFAST})
            dietary_intake_lunch_form.save(user=request.user, field_value={"meal": DietaryIntake.LUNCH})
            dietary_intake_snacks_form.save(user=request.user, field_value={"meal": DietaryIntake.SNACKS})
            dietary_intake_dinner_form.save(user=request.user, field_value={"meal": DietaryIntake.DINNER})
            weight_form.save(user=request.user)
            sleep_patterns_form.save(user=request.user)
            mood_form.save(user=request.user)
            hydration_form.save(user=request.user)
            foot_health_form.save(user=request.user)

            messages.success(request, 'Health data saved successfully.')
            return redirect('health_data_view')

    else:
        blood_glucose_form = BloodGlucoseForm(instance=blood_glucose)
        medication_form = MedicationForm(instance=medication)
        insulin_use_form = InsulinUseForm(instance=insulin_use)
        blood_pressure_form = BloodPressureForm(instance=blood_pressure)
        physical_activity_form = PhysicalActivityForm(instance=physical_activity)
        step_count_form = StepCountForm(instance=step_count)
        dietary_intake_breakfast_form = DietaryIntakeForm(instance=dietary_intake_breakfast, prefix="breakfast")
        dietary_intake_lunch_form = DietaryIntakeForm(instance=dietary_intake_lunch, prefix="lunch")
        dietary_intake_snacks_form = DietaryIntakeForm(instance=dietary_intake_snacks, prefix="snacks")
        dietary_intake_dinner_form = DietaryIntakeForm(instance=dietary_intake_dinner, prefix="dinner")
        weight_form = WeightForm(instance=weight)
        sleep_patterns_form = SleepPatternsForm(instance=sleep_patterns)
        mood_form = MoodAndEmotionalWellBeingForm(instance=mood)
        hydration_form = HydrationForm(instance=hydration)
        foot_health_form = FootHealthCheckForm(instance=foot_health)

    context = {
        'blood_glucose_form': blood_glucose_form,
        'medication_form': medication_form,
        'insulin_use_form': insulin_use_form,
        'blood_pressure_form': blood_pressure_form,
        'physical_activity_form': physical_activity_form,
        'step_count_form': step_count_form,
        'dietary_intake_breakfast_form': dietary_intake_breakfast_form,
        'dietary_intake_lunch_form': dietary_intake_lunch_form,
        'dietary_intake_snacks_form': dietary_intake_snacks_form,
        'dietary_intake_dinner_form': dietary_intake_dinner_form,
        'weight_form': weight_form,
        'sleep_patterns_form': sleep_patterns_form,
        'mood_form': mood_form,
        'hydration_form': hydration_form,
        'foot_health_form': foot_health_form,
    }

    return render(request, 'patient/add_daily_details.html', context)
