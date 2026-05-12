from django.test import TestCase
from django.contrib.auth import get_user_model

from planner_modules.schedule_management.models import Schedule
from .services import ReportService

User = get_user_model()


class ReportTest(TestCase):

    def test_pdf_generation(self):
        user = User.objects.create(username="test")
        Schedule.objects.create(user=user)

        file_path = ReportService.generate_pdf_report(user)

        self.assertTrue(file_path.endswith(".pdf"))

    def test_csv_generation(self):
        user = User.objects.create(username="test")
        Schedule.objects.create(user=user)

        file_path = ReportService.generate_csv_report(user)

        self.assertTrue(file_path.endswith(".csv"))