from django.urls import path
from .services import ReportService
from django.http import FileResponse
from django.contrib.auth.decorators import login_required


@login_required
def download_pdf(request):
    file_path = ReportService.generate_pdf_report(request.user)
    return FileResponse(open(file_path, 'rb'), as_attachment=True)


@login_required
def download_csv(request):
    file_path = ReportService.generate_csv_report(request.user)
    return FileResponse(open(file_path, 'rb'), as_attachment=True)


urlpatterns = [
    path('pdf/', download_pdf, name='download_pdf'),
    path('csv/', download_csv, name='download_csv'),
]