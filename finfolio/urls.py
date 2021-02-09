from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    # url('', views.finfolio_view, name='finfolio'),
    url("trades/", views.trades_view, name='trades'),
    url("trade-form/", views.trade_form_view, name='trade_form'),
    url('', views.portfolio_view, name='portfolio'),
]
