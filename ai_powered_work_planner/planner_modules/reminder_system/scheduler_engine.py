from .services import ReminderService


class SchedulerEngine:

    @staticmethod
    def process_reminders():
        reminders = ReminderService.get_pending_reminders()

        notifications = []

        for reminder in reminders:
            message = f"Reminder: You have a shift at {reminder.shift.start_time}"

            notifications.append({
                "user": reminder.user.username,
                "message": message
            })

            ReminderService.mark_as_sent(reminder)

        return notifications