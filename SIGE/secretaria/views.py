from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def secretaria_login(request):
    return render(request,'secretaria/view_secretary.html',{})
