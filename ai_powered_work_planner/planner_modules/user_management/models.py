from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # =========================
    # ADDITIONAL FIELDS
    # =========================
    full_name = models.CharField(max_length=150, blank=True)

    # Override email safely
    email = models.EmailField(unique=True)

    has_accepted_terms = models.BooleanField(default=False)
    has_viewed_privacy = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    # =========================
    # AUTH CONFIG
    # =========================
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # =========================
    # STRING REPRESENTATION
    # =========================
    def __str__(self):
        return self.username