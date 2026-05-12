from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone

from planner_modules.schedule_management.models import Schedule, Shift
from planner_modules.job_management.models import Job
from .services import AnalyticsService

User = get_user_model()


class AnalyticsTest(TestCase):

    def test_analytics_summary(self):
        user = User.objects.create(username="test")

        schedule = Schedule.objects.create(user=user)
        job = Job.objects.create(user=user, job_name="Test Job", pay_rate=10, location="City")

        Shift.objects.create(
            schedule=schedule,
            job=job,
            start_time=timezone.now(),
            end_time=timezone.now() + timedelta(hours=2)
        )

        summary = AnalyticsService.get_summary(user)

        self.assertIn("total_hours", summary)
        self.assertIn("expected_income", summary)