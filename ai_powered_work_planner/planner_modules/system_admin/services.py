from django.contrib.auth import get_user_model

from planner_modules.ai_planner_engine.model_trainer import ModelTrainer
from planner_modules.ai_planner_engine.workload_predictor import WorkloadPredictor
from planner_modules.ai_planner_engine.conflict_detector import ConflictDetector

from .models import ModelLog


User = get_user_model()


class AdminService:

    @staticmethod
    def get_model_accuracy():
        # Dummy accuracy logic (can be improved later)
        accuracy = 0.85
        ModelLog.objects.create(accuracy=accuracy)
        return accuracy

    @staticmethod
    def retrain_model():
        result = ModelTrainer.train_model()
        return result

    @staticmethod
    def update_overlap_rules():
        # Placeholder for future rule updates
        return "Overlap rules updated successfully"

    @staticmethod
    def get_active_user_count():
        return User.objects.count()

    @staticmethod
    def get_logs():
        return ModelLog.objects.all().order_by('-created_at')