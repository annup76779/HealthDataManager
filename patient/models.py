from django.db import models

from account.models import User


class DailyCheckup(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    # Blood Sugar Levels (recorded before and after meals, and before bedtime)
    blood_sugar_morning = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Before breakfast
    blood_sugar_after_breakfast = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_sugar_before_lunch = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_sugar_after_lunch = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_sugar_before_dinner = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_sugar_after_dinner = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_sugar_before_bedtime = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    # Medication adherence
    medication_taken = models.BooleanField(default=False)  # Did the patient take medication as prescribed?

    # Diet tracking
    diet_details = models.TextField(blank=True, null=True)  # Patient can record diet information, or food log

    # Foot check
    foot_check_completed = models.BooleanField(default=False)  # Whether the patient checked their feet for any issues

    # Exercise tracking
    exercise_minutes = models.IntegerField(blank=True, null=True)  # Duration of exercise in minutes

    # Timestamp for the daily checkup entry
    date_recorded = models.DateField()
    date_updated = models.DateField(auto_now_add=True)  # Automatically add the date when the record is updated

    class Meta:
        verbose_name_plural = 'Daily Checkups'
        ordering = ['-date_updated']  # Orders the records by most recently updated

    def __str__(self):
        return f"Daily Checkup for {self.patient} on {self.date_recorded}"
