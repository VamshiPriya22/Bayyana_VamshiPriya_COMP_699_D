from datetime import datetime


def format_datetime(dt):
    if not dt:
        return ""
    return dt.strftime("%Y-%m-%d %H:%M")


def calculate_hours(start, end):
    if not start or not end:
        return 0
    return (end - start).total_seconds() / 3600


def safe_divide(a, b):
    try:
        return a / b if b != 0 else 0
    except Exception:
        return 0


def round_value(value, digits=2):
    try:
        return round(value, digits)
    except Exception:
        return value