from planner_modules.schedule_management.services import ScheduleService
from .conflict_detector import ConflictDetector


class FeatureProcessor:

    @staticmethod
    def extract_features(user):
        schedule = ScheduleService.get_user_schedule(user)
        shifts = list(schedule.shifts.all())

        total_hours = schedule.total_hours
        job_count = len(set([s.job.id for s in shifts]))

        overlap_count = ConflictDetector.count_conflicts(shifts)
        gaps = ConflictDetector.calculate_gaps(shifts)

        avg_gap = sum(gaps)/len(gaps) if gaps else 0

        return {
            "total_hours": total_hours,
            "job_count": job_count,
            "overlap_count": overlap_count,
            "avg_gap": avg_gap
        }