from django.conf.urls import url, include
from . import views


urlpatterns = [
    url('stocks/', views.stock_list_view, name='stock_list'),
    url('crypto/', views.crypto_list_view, name='crypto_list'),
]
