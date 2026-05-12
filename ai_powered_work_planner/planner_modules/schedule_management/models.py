from django.db import models
from django.conf import settings
from planner_modules.job_management.models import Job


class Schedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    total_hours = models.FloatField(default=0)
    expected_income = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Schedule - {self.user.username}"


class Shift(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='shifts')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.job.job_name} ({self.start_time} - {self.end_time})"