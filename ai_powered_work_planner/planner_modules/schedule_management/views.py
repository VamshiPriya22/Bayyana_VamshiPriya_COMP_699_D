from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ShiftForm
from .models import Shift
from .services import ScheduleService


# =========================
# WEEKLY VIEW (MAIN PAGE)
# =========================
@login_required
def schedule_view(request):
    schedule = ScheduleService.get_user_schedule(request.user)

    shifts = schedule.shifts.all().order_by('start_time')

    return render(request, 'schedule_management/weekly_view.html', {
        'schedule': schedule,
        'shifts': shifts
    })


# =========================
# MONTHLY VIEW
# =========================
@login_required
def monthly_view(request):
    schedule = ScheduleService.get_user_schedule(request.user)

    shifts = schedule.shifts.all().order_by('start_time')

    return render(request, 'schedule_management/monthly_view.html', {
        'shifts': shifts
    })


# =========================
# CREATE SHIFT
# =========================
@login_required
def create_shift_view(request):
    form = ShiftForm(request.POST or None)

    if form.is_valid():
        ScheduleService.create_shift(request.user, form)
        messages.success(request, "Shift added successfully")
        return redirect('schedule')

    return render(request, 'schedule_management/shift_form.html', {
        'form': form
    })


# =========================
# UPDATE SHIFT
# =========================
@login_required
def update_shift_view(request, shift_id):
    shift = get_object_or_404(
        Shift,
        id=shift_id,
        schedule__user=request.user
    )

    form = ShiftForm(request.POST or None, instance=shift)

    if form.is_valid():
        ScheduleService.update_shift(shift, form)
        messages.success(request, "Shift updated successfully")
        return redirect('schedule')

    return render(request, 'schedule_management/shift_form.html', {
        'form': form
    })


# =========================
# DELETE SHIFT
# =========================
@login_required
def delete_shift_view(request, shift_id):
    shift = get_object_or_404(
        Shift,
        id=shift_id,
        schedule__user=request.user
    )

    ScheduleService.delete_shift(shift)
    messages.success(request, "Shift deleted successfully")

    return redirect('schedule')


# =========================
# AVAILABILITY (NEW)
# =========================
@login_required
def availability_view(request):
    if request.method == "POST":
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        ScheduleService.update_availability(
            request.user,
            start_time,
            end_time
        )

        messages.success(request, "Availability updated successfully")
        return redirect('schedule')

    return render(request, 'schedule_management/availability.html')