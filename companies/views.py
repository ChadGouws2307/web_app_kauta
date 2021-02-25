from django.shortcuts import render

from .models import CompanyStock, CryptoCurrency


def stock_list_view(request):
    stocks = CompanyStock.objects.all().order_by('name')

    context = {
        'stocks': stocks,
    }

    return render(request, "stock_list.html", context)


def crypto_list_view(request):
    cryptos = CryptoCurrency.objects.all().order_by('name')

    context = {
        'cryptos': cryptos,
    }

    return render(request, "crypto_list.html", context)
