from django.conf.urls import url
from . import views


urlpatterns = [
    url("trades/", views.trades_view, name='trades'),
    url("trade-form/", views.trade_form_view, name='trade_form'),
    url("trade-upload/", views.trade_file_upload_view, name='trade_file_upload'),
    url("how-to-upload-trade-file/", views.how_to_upload_trade_file_view, name='how_to_upload_trade_file'),
    url('', views.portfolio_view, name='portfolio'),
]
