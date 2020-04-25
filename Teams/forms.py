from django import forms
from django.forms import ModelForm

from .models import *

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

