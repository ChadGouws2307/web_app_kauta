from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.db.models import Avg, Sum, Count, F, FloatField, ExpressionWrapper

from .models import Trade, CompanyStock
from .forms import TradeForm


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
        prices = trades.aggregate(w_avg=ExpressionWrapper(Sum((F('no_of_shares')*F('price')))/Sum(F('no_of_shares')), output_field=FloatField()))
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


def finfolio_view(request):
    return redirect('trade_form')


if __name__ == '__main__':
    a = portfolio_view()
    print(a)
