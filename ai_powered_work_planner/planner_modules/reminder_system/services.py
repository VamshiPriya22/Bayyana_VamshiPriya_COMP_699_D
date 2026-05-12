from datetime import timedelta
from django.utils import timezone
from .models import Reminder


class ReminderService:

    @staticmethod
    def create_reminder(user, shift, minutes_before):
        reminder_time = shift.start_time - timedelta(minutes=minutes_before)

        reminder = Reminder.objects.create(
            user=user,
            shift=shift,
            remind_before_minutes=minutes_before,
            reminder_time=reminder_time
        )

        return reminder

    @staticmethod
    def get_user_reminders(user):
        return Reminder.objects.filter(user=user).order_by('-reminder_time')

    @staticmethod
    def get_pending_reminders():
        now = timezone.now()
        return Reminder.objects.filter(reminder_time__lte=now, is_sent=False)

    @staticmethod
    def mark_as_sent(reminder):
        reminder.is_sent = True
        reminder.save()