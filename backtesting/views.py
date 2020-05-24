from django.shortcuts import render

from .models import Statergies


# Create your views here.
def backtesting_home(request):
    return render(request, 'backtesting/backtesting-home.html')

