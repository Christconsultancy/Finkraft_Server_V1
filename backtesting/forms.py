from django import forms
from django.forms import ModelForm

from .models import Statergies


def AddStatergy(ModelForm):
    class Meta:
        model = Statergies
        fields = ['statergy_name', 'statergy_status']
        labels = {
            'statergy_name': 'Statergy Name',
            'statergy_status': 'Statergy Status',
        }
