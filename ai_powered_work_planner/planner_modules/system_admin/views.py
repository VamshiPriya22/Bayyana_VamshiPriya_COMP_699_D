from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .services import AdminService


@login_required
def admin_dashboard_view(request):
    accuracy = AdminService.get_model_accuracy()
    user_count = AdminService.get_active_user_count()
    logs = AdminService.get_logs()

    return render(request, 'admin_panel/dashboard.html', {
        "accuracy": accuracy,
        "user_count": user_count,
        "logs": logs
    })


@login_required
def retrain_model_view(request):
    result = AdminService.retrain_model()
    messages.success(request, result)
    return redirect('admin_dashboard')


@login_required
def update_rules_view(request):
    result = AdminService.update_overlap_rules()
    messages.success(request, result)
    return redirect('admin_dashboard')