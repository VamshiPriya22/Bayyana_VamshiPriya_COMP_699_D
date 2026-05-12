from django.test import TestCase
from django.contrib.auth import get_user_model
from planner_modules.job_management.models import Job
from .models import Schedule

User = get_user_model()


class ScheduleTest(TestCase):

    def test_schedule_creation(self):
        user = User.objects.create(username="test")
        schedule = Schedule.objects.create(user=user)

        self.assertEqual(schedule.user.username, "test")