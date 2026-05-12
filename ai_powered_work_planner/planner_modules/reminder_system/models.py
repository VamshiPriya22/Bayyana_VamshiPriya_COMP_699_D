from django.db import models
from django.conf import settings
from planner_modules.schedule_management.models import Shift


class Reminder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    remind_before_minutes = models.IntegerField(default=30)

    reminder_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.user.username} - {self.shift}"