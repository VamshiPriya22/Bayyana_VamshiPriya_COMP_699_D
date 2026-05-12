import os
from django.conf import settings

from .pdf_generator import PDFGenerator
from .csv_generator import CSVGenerator


class ReportService:

    @staticmethod
    def generate_pdf_report(user):
        file_path = os.path.join(settings.MEDIA_ROOT, f"{user.username}_schedule.pdf")
        return PDFGenerator.generate_schedule_pdf(user, file_path)

    @staticmethod
    def generate_csv_report(user):
        file_path = os.path.join(settings.MEDIA_ROOT, f"{user.username}_schedule.csv")
        return CSVGenerator.generate_schedule_csv(user, file_path)