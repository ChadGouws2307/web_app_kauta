from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    url("accounts/", include("django.contrib.auth.urls")),
    # url("dashboard/", views.dashboard_view, name="dashboard"),
    # url('us-election/', views.election_view, name='election'),
    # url("register/", views.register, name="register"),
    path('signup/', views.signup_view, name="signup"),
    path('signup_/', views.signup_view_v2, name="signup_v2"),
    path('success/', views.success_view, name="success"),
    path('login/', views.login_view, name="login"),
]
