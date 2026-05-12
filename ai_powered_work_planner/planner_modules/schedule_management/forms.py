from django import forms
from .models import Shift


class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['job', 'start_time', 'end_time']

        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }