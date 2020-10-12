from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_view, name="about"),
    path('', views.pricing_view, name='pricing'),
]
