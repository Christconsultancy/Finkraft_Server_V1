from django.contrib import admin

from .models import Statergies
# Register your models here.
backtesting_models = [Statergies]

admin.site.register(backtesting_models)