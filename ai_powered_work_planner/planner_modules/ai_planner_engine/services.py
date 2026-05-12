from .feature_processor import FeatureProcessor
from .workload_predictor import WorkloadPredictor
from .rest_recommender import RestRecommender
from .conflict_detector import ConflictDetector
from planner_modules.schedule_management.services import ScheduleService


class AIService:

    @staticmethod
    def analyze_user_schedule(user):
        print("🔥 AI SERVICE CALLED")

        # =========================
        # FETCH SCHEDULE
        # =========================
        schedule = ScheduleService.get_user_schedule(user)

        if not schedule:
            print("❌ No schedule found")
            return {
                "workload": "Low",
                "features": {
                    "total_hours": 0,
                    "job_count": 0,
                    "overlap_count": 0,
                    "avg_gap": 0
                },
                "suggestions": ["No schedule found. Please add shifts."],
                "conflicts": []
            }

        shifts = list(schedule.shifts.all())
        print("📅 Total shifts:", len(shifts))

        # =========================
        # HANDLE EMPTY SHIFTS
        # =========================
        if not shifts:
            print("⚠ No shifts available")
            return {
                "workload": "Low",
                "features": {
                    "total_hours": 0,
                    "job_count": 0,
                    "overlap_count": 0,
                    "avg_gap": 0
                },
                "suggestions": ["No shifts added yet. Start scheduling your work."],
                "conflicts": []
            }

        # =========================
        # FEATURE EXTRACTION
        # =========================
        features = FeatureProcessor.extract_features(user)
        print("📊 Features:", features)

        # =========================
        # WORKLOAD PREDICTION
        # =========================
        predictor = WorkloadPredictor()
        workload = predictor.predict(features)
        print("🧠 Workload:", workload)

        # =========================
        # SUGGESTIONS
        # =========================
        suggestions = RestRecommender.suggest(features)
        print("💡 Suggestions:", suggestions)

        # =========================
        # CONFLICT DETECTION
        # =========================
        raw_conflicts = ConflictDetector.detect_conflicts(shifts)
        print("⚠ Raw Conflicts:", raw_conflicts)

        formatted_conflicts = []

        for s1, s2 in raw_conflicts:
            conflict_text = (
                f"{s1.job.job_name} "
                f"({s1.start_time.strftime('%I:%M %p')}) overlaps with "
                f"{s2.job.job_name} "
                f"({s2.start_time.strftime('%I:%M %p')})"
            )
            formatted_conflicts.append(conflict_text)

        # =========================
        # FINAL RESPONSE
        # =========================
        return {
            "workload": workload,
            "features": features,
            "suggestions": suggestions,
            "conflicts": formatted_conflicts
        }