from django.test import TestCase
from django.contrib.auth import get_user_model
from planner_modules.schedule_management.models import Schedule

from .services import AIService

User = get_user_model()


class AITest(TestCase):

    def test_ai_analysis(self):
        user = User.objects.create(username="test")
        Schedule.objects.create(user=user)

        result = AIService.analyze_user_schedule(user)

        self.assertIn("workload", result)