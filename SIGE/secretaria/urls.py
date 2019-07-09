from django.urls import path
from . import views

urlpatterns = [
    path('', views.secretaria_login, name='secretaria_login')
]
