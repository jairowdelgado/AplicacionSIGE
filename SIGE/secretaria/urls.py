from django.urls import path
from . import views
from django.conf.urls import include, url
from electivas import urls

urlpatterns = [
    path('Home', views.secretaria_login, name='secretaria_login'),
    path('',include('electivas.urls'),name='gestion_electivas'),
]
