"""SIGE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('secretaria/', include('secretaria.urls')),
    path('electivas/', include('electivas.urls')),
    path('admin/', admin.site.urls),

    # url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'accounts/logout/$',logout_controller,name='logout'),

    # path('secretaria/',secretaria,name='secretaria')


    #electivas
    #url(r'^cursos/', include('electivas.urls', namespace='electivas')),
    #path('electivas', electivas.views.ElectivaList.as_view(), name='elctiva_list'),
    #path('contact/<int:pk>', electivas.views.ElectivaDetail.as_view(), name='elctiva_detail'),
    #path('create', electivas.views.ElectivaCreation.as_view(), name='elctiva_create'),
    #path('update/<int:pk>', electivas.views.ElectivaUpdate.as_view(), name='elctiva_update'),
    #path('delete/<int:pk>', electivas.views.ElectivaDelete.as_view(), name='elctiva_delete'),

]
