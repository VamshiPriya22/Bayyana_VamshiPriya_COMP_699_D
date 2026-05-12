import csv
from planner_modules.schedule_management.services import ScheduleService


class CSVGenerator:

    @staticmethod
    def generate_schedule_csv(user, file_path):
        schedule = ScheduleService.get_user_schedule(user)
        shifts = schedule.shifts.all()

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["Job", "Start Time", "End Time", "Hours"])

            for shift in shifts:
                hours = (shift.end_time - shift.start_time).total_seconds() / 3600

                writer.writerow([
                    shift.job.job_name,
                    shift.start_time,
                    shift.end_time,
                    round(hours, 2)
                ])

        return file_path