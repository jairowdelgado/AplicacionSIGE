from django.shortcuts import render
from django.views.decorators.http import require_POST
from electivas import views
# Create your views here.

#@require_POST
def secretaria_login(request):
    return render(request,'view_secretary.html',{})

def gestionar_electivas(request):
    return render(request,'electivas')