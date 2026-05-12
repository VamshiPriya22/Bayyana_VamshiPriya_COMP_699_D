from django.core.exceptions import ValidationError


def validate_password_strength(password):
    if len(password) < 6:
        raise ValidationError("Password must be at least 6 characters long.")