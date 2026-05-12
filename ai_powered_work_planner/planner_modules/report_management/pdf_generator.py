from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

from planner_modules.schedule_management.services import ScheduleService


class PDFGenerator:

    @staticmethod
    def generate_schedule_pdf(user, file_path):
        schedule = ScheduleService.get_user_schedule(user)
        shifts = schedule.shifts.all()

        doc = SimpleDocTemplate(file_path, pagesize=letter)

        data = [["Job", "Start Time", "End Time", "Hours"]]

        for shift in shifts:
            hours = (shift.end_time - shift.start_time).total_seconds() / 3600

            data.append([
                shift.job.job_name,
                str(shift.start_time),
                str(shift.end_time),
                round(hours, 2)
            ])

        table = Table(data)

        elements = [table]
        doc.build(elements)

        return file_path