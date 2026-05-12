from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Job

User = get_user_model()


class JobTest(TestCase):

    def test_create_job(self):
        user = User.objects.create(username="test")
        job = Job.objects.create(user=user, job_name="Test Job", pay_rate=10, location="City")

        self.assertEqual(job.job_name, "Test Job")