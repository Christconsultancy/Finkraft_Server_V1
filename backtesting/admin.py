from django.contrib import admin

from .models import Statergies, Stock

# Register your models here.
backtesting_models = [Statergies, Stock]

admin.site.register(backtesting_models)
