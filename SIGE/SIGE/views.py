from django.shortcuts import redirect
from django.contrib import auth
from django.shortcuts import render

def login(request):
    return render(request,'registration/login.html')
 