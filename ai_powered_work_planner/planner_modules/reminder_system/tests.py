from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone

from planner_modules.schedule_management.models import Schedule, Shift
from planner_modules.job_management.models import Job
from .services import ReminderService

User = get_user_model()


class ReminderTest(TestCase):

    def test_create_reminder(self):
        user = User.objects.create(username="test")

        schedule = Schedule.objects.create(user=user)
        job = Job.objects.create(user=user, job_name="Test", pay_rate=10, location="City")

        shift = Shift.objects.create(
            schedule=schedule,
            job=job,
            start_time=timezone.now() + timedelta(hours=2),
            end_time=timezone.now() + timedelta(hours=4)
        )

        reminder = ReminderService.create_reminder(user, shift, 30)

        self.assertEqual(reminder.user, user)