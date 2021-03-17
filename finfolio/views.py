from django.shortcuts import render, redirect
from django.db.models import Avg, Sum, Count, F, FloatField, ExpressionWrapper

from companies.models import CompanyStock
from .models import Trade
from .forms import TradeForm, TradeFileForm
from .file_processing import process_trade_file


def trades_view(request):
    user_trades = Trade.objects.filter(user=request.user).order_by('-date')

    context = {
        'user_trades': user_trades,
    }
    return render(request, "trades.html", context)


def portfolio_view(request):
    user_portfolio = []
    for stock in CompanyStock.objects.all().order_by('name'):
        all_trades = Trade.objects.filter(user=request.user).filter(company=stock)
        shares = all_trades.aggregate(sum=Sum('no_of_shares'))
        if shares['sum'] is not None:
            if shares['sum'] > 0:
                trades = all_trades.filter(no_of_shares__gte=0)             # No of shares >= 0
            elif shares['sum'] < 0:
                trades = all_trades.filter(no_of_shares__lte=0)             # No of shares <= 0
            else:
                continue
        else:
            continue
        prices = trades.aggregate(w_avg=ExpressionWrapper(Sum((F('no_of_shares')*F('price')))/Sum(F('no_of_shares')),
                                                          output_field=FloatField()))
        user_portfolio.append([str(stock), str(stock.ticker), shares['sum'], prices['w_avg']])

    context = {
        'user_portfolio': user_portfolio
    }
    return render(request, "portfolio.html", context)


def trade_form_view(request):

    form = TradeForm(request.POST or None)

    if form.is_valid():
        trade = form.save(commit=False)
        trade.user = request.user
        trade.save()
        return redirect('trade_form')

    return render(request, 'trade_form.html', {'form': form})


def trade_file_upload_view(request):
    if request.method == 'POST':
        form = TradeFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['trade_file']
            if str(file).endswith('.csv'):
                process_trade_file(file, request.user)
                ind = 'File uploaded successfully - please see your List of Trades to confirm'
                return render(request, 'upload_trade_file.html', {'form': form, 'upload_ind': ind})
            else:
                ind = 'File type is incorrect, must be .CSV'
                return render(request, 'upload_trade_file.html', {'form': form, 'upload_ind': ind})
        else:
            pass
    else:
        form = TradeFileForm()
    return render(request, 'upload_trade_file.html', {'form': form})


def how_to_upload_trade_file_view(request):
    data = {
        'trades': [['amzn', '01-03-2021', '2500', '100'],
                   ['aapl', '28-02-2021', '120', '500'],
                   ['fb', '23-01-2021', '90', '803'],
                   ['aapl', '01-01-2021', '110', '400'],
                   ['aapl', '21-12-2020', '100', '450'],
                   ['fb', '23-11-2020', '95', '302'],
                   ['amzn', '01-09-2020', '115', '300']]
    }
    return render(request, 'how_to_upload_trade_file.html', data)
