from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required
def login_controller(request):
    pass


def logout_controller(request):
    auth.logout(request)
    return redirect('/accounts/login')    