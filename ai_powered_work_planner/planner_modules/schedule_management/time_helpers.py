from datetime import timedelta


def calculate_hours(start, end):
    duration = end - start
    return duration.total_seconds() / 3600


def calculate_gap(prev_end, next_start):
    gap = next_start - prev_end
    return gap.total_seconds() / 3600