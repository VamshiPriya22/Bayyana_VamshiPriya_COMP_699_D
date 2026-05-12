from planner_modules.schedule_management.services import ScheduleService


class AnalyticsService:

    # =========================
    # TOTAL HOURS
    # =========================
    @staticmethod
    def get_total_hours(user):
        schedule = ScheduleService.get_user_schedule(user)

        shifts = schedule.shifts.all()

        if not shifts:
            return 0

        total = 0
        for shift in shifts:
            total += (shift.end_time - shift.start_time).total_seconds() / 3600

        return round(total, 2)

    # =========================
    # EXPECTED INCOME
    # =========================
    @staticmethod
    def get_expected_income(user):
        schedule = ScheduleService.get_user_schedule(user)

        shifts = schedule.shifts.all()

        if not shifts:
            return 0

        total_income = 0
        for shift in shifts:
            hours = (shift.end_time - shift.start_time).total_seconds() / 3600
            total_income += hours * shift.job.pay_rate

        return round(total_income, 2)

    # =========================
    # JOB-WISE INCOME
    # =========================
    @staticmethod
    def get_job_wise_income(user):
        schedule = ScheduleService.get_user_schedule(user)
        shifts = schedule.shifts.all()

        job_income = {}

        for shift in shifts:
            hours = (shift.end_time - shift.start_time).total_seconds() / 3600
            income = hours * shift.job.pay_rate

            job_name = shift.job.job_name

            if job_name not in job_income:
                job_income[job_name] = 0

            job_income[job_name] += income

        return {k: round(v, 2) for k, v in job_income.items()}

    # =========================
    # DAILY HOURS
    # =========================
    @staticmethod
    def get_daily_hours(user):
        schedule = ScheduleService.get_user_schedule(user)
        shifts = schedule.shifts.all()

        daily_hours = {}

        for shift in shifts:
            date = shift.start_time.date()

            hours = (shift.end_time - shift.start_time).total_seconds() / 3600

            if date not in daily_hours:
                daily_hours[date] = 0

            daily_hours[date] += hours

        # SORT BY DATE (IMPORTANT FOR UI)
        sorted_data = dict(sorted(daily_hours.items()))

        return {str(k): round(v, 2) for k, v in sorted_data.items()}

    # =========================
    # SUMMARY (USED IN DASHBOARD)
    # =========================
    @staticmethod
    def get_summary(user):
        return {
            "total_hours": AnalyticsService.get_total_hours(user),
            "expected_income": AnalyticsService.get_expected_income(user),
            "job_wise_income": AnalyticsService.get_job_wise_income(user),
            "daily_hours": AnalyticsService.get_daily_hours(user),
        }