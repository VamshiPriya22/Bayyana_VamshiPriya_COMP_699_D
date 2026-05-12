from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class UserService:

    @staticmethod
    def authenticate_user(request, username, password):
        return authenticate(request, username=username, password=password)

    @staticmethod
    def update_profile(user, form):
        user.full_name = form.cleaned_data['full_name']
        user.email = form.cleaned_data['email']
        user.save()

    @staticmethod
    def reset_password(user, new_password):
        user.password = make_password(new_password)
        user.save()

    @staticmethod
    def accept_terms(user):
        user.has_accepted_terms = True
        user.save()

    @staticmethod
    def mark_privacy_viewed(user):
        user.has_viewed_privacy = True
        user.save()