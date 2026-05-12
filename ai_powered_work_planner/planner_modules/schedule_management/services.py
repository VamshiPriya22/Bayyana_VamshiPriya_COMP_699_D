from .models import Schedule, Shift
from .time_helpers import calculate_hours


class ScheduleService:

    @staticmethod
    def get_or_create_schedule(user):
        schedule, created = Schedule.objects.get_or_create(user=user)
        return schedule

    @staticmethod
    def create_shift(user, form):
        schedule = ScheduleService.get_or_create_schedule(user)

        shift = form.save(commit=False)
        shift.schedule = schedule
        shift.save()

        ScheduleService.update_schedule_metrics(schedule)

        return shift

    @staticmethod
    def update_shift(shift, form):
        shift.job = form.cleaned_data['job']
        shift.start_time = form.cleaned_data['start_time']
        shift.end_time = form.cleaned_data['end_time']
        shift.save()

        ScheduleService.update_schedule_metrics(shift.schedule)

    @staticmethod
    def delete_shift(shift):
        schedule = shift.schedule
        shift.delete()
        ScheduleService.update_schedule_metrics(schedule)

    @staticmethod
    def update_schedule_metrics(schedule):
        shifts = schedule.shifts.all()

        total_hours = 0
        total_income = 0

        for shift in shifts:
            hours = calculate_hours(shift.start_time, shift.end_time)
            total_hours += hours
            total_income += hours * shift.job.pay_rate

        schedule.total_hours = total_hours
        schedule.expected_income = total_income
        schedule.save()

    @staticmethod
    def get_user_schedule(user):
        return ScheduleService.get_or_create_schedule(user)