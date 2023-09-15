from django import forms
from django.forms import TextInput, EmailInput, DateInput, Select

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course', 'email', 'department',   'active', 'profile']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course':  TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter course'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': ' Please enter your email'}),
            'department': Select(attrs={'class': 'form-select'}),

        }