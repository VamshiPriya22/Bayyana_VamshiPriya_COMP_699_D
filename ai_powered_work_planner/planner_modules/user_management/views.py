from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, LoginForm, ProfileForm, PasswordResetForm
from .services import UserService

# AI + SYSTEM SERVICES
from planner_modules.ai_planner_engine.services import AIService
from planner_modules.analytics_engine.services import AnalyticsService
from planner_modules.schedule_management.services import ScheduleService


# =========================
# REGISTER
# =========================
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "✅ Account created successfully")
            return redirect('dashboard')
        else:
            print("❌ REGISTER FORM ERRORS:", form.errors)
            messages.error(request, "Please correct the errors below")
    else:
        form = RegisterForm()

    return render(request, 'user_management/register.html', {'form': form})


# =========================
# LOGIN
# =========================
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = UserService.authenticate_user(
                request,
                form.cleaned_data['username'],
                form.cleaned_data['password']
            )

            if user:
                login(request, user)
                messages.success(request, "✅ Login successful")
                return redirect('dashboard')
            else:
                messages.error(request, "❌ Invalid username or password")
        else:
            print("❌ LOGIN FORM ERRORS:", form.errors)
    else:
        form = LoginForm()

    return render(request, 'user_management/login.html', {'form': form})


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('login')


# =========================
# DASHBOARD (🔥 FULL FIXED VERSION)
# =========================
@login_required
def dashboard_view(request):
    user = request.user

    try:
        print("🚀 Loading Dashboard for:", user)

        # =========================
        # AI DATA
        # =========================
        ai_data = AIService.analyze_user_schedule(user)
        print("AI DATA:", ai_data)

        # =========================
        # ANALYTICS DATA
        # =========================
        analytics_data = AnalyticsService.get_summary(user)
        print("ANALYTICS:", analytics_data)

        # =========================
        # SCHEDULE DATA
        # =========================
        schedule = ScheduleService.get_user_schedule(user)

        if schedule:
            shifts = schedule.shifts.all().order_by('start_time')[:5]
            print("SHIFTS COUNT:", shifts.count())
        else:
            print("⚠ No schedule found")
            shifts = []

    except Exception as e:
        print("❌ DASHBOARD ERROR:", str(e))

        # SAFE FALLBACK (IMPORTANT)
        ai_data = {
            "workload": "Low",
            "features": {
                "total_hours": 0,
                "job_count": 0,
                "overlap_count": 0,
                "avg_gap": 0
            },
            "suggestions": ["Error loading AI data"],
            "conflicts": []
        }

        analytics_data = {
            "total_hours": 0,
            "income": 0
        }

        shifts = []

    context = {
        "ai": ai_data,
        "analytics": analytics_data,
        "shifts": shifts,
    }

    return render(request, 'dashboard/dashboard.html', context)


# =========================
# PROFILE
# =========================
@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            UserService.update_profile(request.user, form)
            messages.success(request, "✅ Profile updated successfully")
            return redirect('profile')
        else:
            print("❌ PROFILE FORM ERRORS:", form.errors)
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'user_management/profile.html', {'form': form})


# =========================
# RESET PASSWORD
# =========================
@login_required
def reset_password_view(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            UserService.reset_password(
                request.user,
                form.cleaned_data['new_password']
            )
            messages.success(request, "✅ Password updated successfully")
            return redirect('profile')
        else:
            print("❌ PASSWORD RESET ERRORS:", form.errors)
    else:
        form = PasswordResetForm()

    return render(request, 'user_management/reset_password.html', {'form': form})


# =========================
# PRIVACY
# =========================
@login_required
def privacy_view(request):
    UserService.mark_privacy_viewed(request.user)
    return render(request, 'user_management/privacy_policy.html')


# =========================
# ACCEPT TERMS
# =========================
@login_required
def accept_terms_view(request):
    UserService.accept_terms(request.user)
    messages.success(request, "✅ Terms accepted successfully")
    return redirect('dashboard')