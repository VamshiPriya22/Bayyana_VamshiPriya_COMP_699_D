from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def handle_exceptions(view_func):
    """Decorator to handle exceptions globally"""

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('dashboard')

    return wrapper


def admin_required(view_func):
    """Allow only admin users"""

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, "Admin access required")
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)

    return wrapper