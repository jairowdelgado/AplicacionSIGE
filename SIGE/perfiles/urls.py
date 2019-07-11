from django.urls import path

from . import views

urlpatterns = [
    path('',views.logout_controller,name='logout')
]
#path('logout',logout, name='logout',kwargs={'next_page':'/'}),