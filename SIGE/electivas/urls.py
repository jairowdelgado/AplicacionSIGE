from django.urls import path
from . import views

urlpatterns = [
    path('', views.ElectivaList.as_view(), name='electivas')
]
