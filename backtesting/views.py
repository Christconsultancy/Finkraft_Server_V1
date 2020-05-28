from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.text import slugify

from .models import Statergies, Stock
from strategies_code.strategies import ema


# Create your views here.
def backtesting_home(request):
    return render(request, 'backtesting/backtesting-home.html')


def single_statergy_test(request):
    statergies = Statergies.objects.all().order_by('statergy_status')

    # pagination
    paginator = Paginator(statergies, 20)  # Show 20 statergies per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'backtesting/signle-statergy.html', context)


def test_statergy(request, statergy):
    try:
        statergy_selected = Statergies.objects.get(statergy_name__icontains=statergy)
        if slugify(statergy_selected.statergy_name) == statergy:
            stock_list = Stock.objects.all()
            hello = "hello"
            if request.POST:
                if "start_date" in request.POST:
                    start_date = request.POST["start_date"]
                    end_date = request.POST["end_date"]
                    timeframe = request.POST["timeframeRadioOptions"]
                    print(start_date, end_date, timeframe)
                    ema_result = ema(start_date, end_date, timeframe)
                    print(ema_result)
            context = {
                'statergy_selected': statergy_selected,
                'stock_list': stock_list,
            }
            return render(request, 'backtesting/test-statergy.html', context)
        else:
            return redirect('backtesting')
    except Exception:
        return redirect('backtesting')
