from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    url("accounts/", include("django.contrib.auth.urls")),
    path('signup/', views.signup_view, name="signup"),
    path('success/', views.success_view, name="success"),
    path('login/', views.login_view, name="login"),
]
