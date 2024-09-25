from django.db import models

from account.models import User


class BloodGlucose(models.Model):
    FASTING = 'Fasting'
    POSTPRANDIAL = 'Postprandial'
    BEDTIME = 'Bedtime'

    READING_TYPE_CHOICES = [
        (FASTING, 'Fasting'),
        (POSTPRANDIAL, 'Postprandial'),
        (BEDTIME, 'Bedtime'),
    ]

    reading_type = models.CharField(max_length=20, choices=READING_TYPE_CHOICES)
    glucose_level = models.DecimalField(max_digits=5, decimal_places=2)  # supports both mg/dL and mmol/L
    time_of_reading = models.TimeField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class Medication(models.Model):
    MEDICATION_CHOICES = [
        ('Metformin', 'Metformin'),
        ('Insulin', 'Insulin'),
        # Add more common medications as needed
    ]
    name = models.CharField(max_length=100, choices=MEDICATION_CHOICES)
    dose = models.DecimalField(max_digits=5, decimal_places=2)
    time_taken = models.TimeField()
    missed_dose = models.BooleanField(default=False)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class InsulinUse(models.Model):
    LONG_ACTING = 'Long-acting'
    RAPID_ACTING = 'Rapid-acting'

    INSULIN_TYPE_CHOICES = [
        (LONG_ACTING, 'Long-acting'),
        (RAPID_ACTING, 'Rapid-acting'),
    ]

    insulin_type = models.CharField(max_length=20, choices=INSULIN_TYPE_CHOICES)
    dose_units = models.DecimalField(max_digits=5, decimal_places=2)
    time_of_administration = models.TimeField()
    injection_site = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class BloodPressure(models.Model):
    systolic = models.PositiveIntegerField()  # mmHg
    diastolic = models.PositiveIntegerField()  # mmHg
    time_of_reading = models.TimeField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class PhysicalActivity(models.Model):
    WALKING = 'Walking'
    RUNNING = 'Running'
    CYCLING = 'Cycling'
    STRENGTH_TRAINING = 'Strength Training'

    EXERCISE_CHOICES = [
        (WALKING, 'Walking'),
        (RUNNING, 'Running'),
        (CYCLING, 'Cycling'),
        (STRENGTH_TRAINING, 'Strength Training'),
    ]

    LOW = 'Low'
    MODERATE = 'Moderate'
    HIGH = 'High'

    INTENSITY_CHOICES = [
        (LOW, 'Low'),
        (MODERATE, 'Moderate'),
        (HIGH, 'High'),
    ]

    exercise_type = models.CharField(max_length=50, choices=EXERCISE_CHOICES)
    duration = models.PositiveIntegerField()  # Minutes
    intensity = models.CharField(max_length=20, choices=INTENSITY_CHOICES)
    time_of_exercise = models.TimeField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class StepCount(models.Model):
    total_steps = models.PositiveIntegerField()
    daily_goal = models.PositiveIntegerField(blank=True, null=True)  # Optional
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class DietaryIntake(models.Model):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    SNACKS = 'Snacks'

    MEAL_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (SNACKS, 'Snacks'),
    ]

    meal = models.CharField(max_length=20, choices=MEAL_CHOICES)
    carb_intake = models.DecimalField(max_digits=5, decimal_places=2)  # Grams
    sugary_foods = models.TextField(blank=True, null=True)  # Optional field
    time_of_meal = models.TimeField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class Weight(models.Model):
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # kg or lbs
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class SleepPatterns(models.Model):
    GOOD = 'Good'
    FAIR = 'Fair'
    POOR = 'Poor'

    SLEEP_QUALITY_CHOICES = [
        (GOOD, 'Good'),
        (FAIR, 'Fair'),
        (POOR, 'Poor'),
    ]

    sleep_duration = models.DecimalField(max_digits=4, decimal_places=2)  # Hours
    sleep_quality = models.CharField(max_length=10, choices=SLEEP_QUALITY_CHOICES)
    wake_up_time = models.TimeField()
    bedtime = models.TimeField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class MoodAndEmotionalWellBeing(models.Model):
    mood_rating = models.PositiveIntegerField()  # 1–10 scale
    notable_events = models.TextField(blank=True, null=True)  # Optional
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class Hydration(models.Model):
    water_intake = models.DecimalField(max_digits=4, decimal_places=2)  # Liters or glasses
    dehydration_symptoms = models.BooleanField(default=False)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class FootHealthCheck(models.Model):
    foot_check_completed = models.BooleanField(default=False)
    abnormalities = models.TextField(blank=True, null=True)  # Optional field for abnormalities like swelling, sores
    pain_level = models.PositiveIntegerField(blank=True, null=True)  # Optional, 1–10 scale
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)


class AssignedToDoctor(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_logs", primary_key=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    assigned_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')
