from django.shortcuts import render

from .models import Statergies
from .forms import AddStatergy


# Create your views here.
def backtesting_home(request):
    return render(request, 'backtesting/backtesting-home.html')


def new_statergy(request):
    current_statergies = Statergies.objects.all()
    add_form = AddStatergy()
    context = {
        'add_form': add_form
    }
    return render(request, 'backtesting/new-statergy.html', context)
