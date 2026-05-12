from django.db import models


class ModelLog(models.Model):
    accuracy = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Accuracy: {self.accuracy} at {self.created_at}"