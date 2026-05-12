from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .validators import validate_password_strength


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'password1', 'password2']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        validate_password_strength(password)
        return password


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email']


class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)