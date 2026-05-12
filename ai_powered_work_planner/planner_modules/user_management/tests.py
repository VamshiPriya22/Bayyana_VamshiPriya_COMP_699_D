from django.test import TestCase
from .models import CustomUser


class UserTest(TestCase):

    def test_user_creation(self):
        user = CustomUser.objects.create(username="test", full_name="Test User")
        self.assertEqual(user.username, "test")