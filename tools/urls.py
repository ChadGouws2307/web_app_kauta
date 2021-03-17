from django.conf.urls import url
from . import views


urlpatterns = [
    url("stock-pca/", views.upload_pca_file_view, name='pca_file_upload'),
    url("how-to-pca/", views.how_to_pca_view, name='how_to_pca'),
]
