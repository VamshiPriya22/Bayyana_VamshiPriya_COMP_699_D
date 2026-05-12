from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import JobForm
from .services import JobService
from .models import Job


@login_required
def job_list_view(request):
    jobs = JobService.get_user_jobs(request.user)
    return render(request, 'job_management/job_list.html', {'jobs': jobs})


@login_required
def create_job_view(request):
    form = JobForm(request.POST or None)

    if form.is_valid():
        JobService.create_job(request.user, form)
        messages.success(request, "Job added successfully")
        return redirect('job_list')

    return render(request, 'job_management/job_form.html', {'form': form})


@login_required
def update_job_view(request, job_id):
    job = get_object_or_404(Job, id=job_id, user=request.user)
    form = JobForm(request.POST or None, instance=job)

    if form.is_valid():
        JobService.update_job(job, form)
        messages.success(request, "Job updated successfully")
        return redirect('job_list')

    return render(request, 'job_management/job_edit.html', {'form': form})


@login_required
def delete_job_view(request, job_id):
    job = get_object_or_404(Job, id=job_id, user=request.user)
    JobService.delete_job(job)
    messages.success(request, "Job deleted")
    return redirect('job_list')