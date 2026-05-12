from django.test import TestCase
from .services import AdminService


class AdminTest(TestCase):

    def test_model_accuracy(self):
        accuracy = AdminService.get_model_accuracy()
        self.assertTrue(accuracy > 0)

    def test_user_count(self):
        count = AdminService.get_active_user_count()
        self.assertEqual(count, 0)