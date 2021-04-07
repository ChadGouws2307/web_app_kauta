from django.conf.urls import url
from . import views


urlpatterns = [
    url("group-stock-correlation/", views.upload_corr_file_view, name='corr_file_upload'),
    url("how-to-stock-correlation/", views.how_to_corr_view, name='how_to_corr'),
]
