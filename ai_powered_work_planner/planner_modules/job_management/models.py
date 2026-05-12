from django.db import models
from django.conf import settings


class Job(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    job_name = models.CharField(max_length=150)
    pay_rate = models.FloatField()
    location = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_name} - {self.user.username}"