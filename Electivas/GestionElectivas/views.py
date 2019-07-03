from django.shortcuts import render,redirect
from .models import Electiva
from django.contrib.auth import authenticate, login
# Create your views here.


def login(request):
    electivas = Electiva.objects.all()
    context = {'electiva': electivas}
    
    return render(request,'IniciarSesion.html',context=context)

def index(request):
    
    if request.method == 'POST':
        name=request.POST.get('username')
        password = request.POST.get('password')
        try:
            electiva = Electiva.objects.get(name=name,password=password)
            context = {'electiva': electiva}
            return render(request,'index.html',context=context)
        except:
            
        #electiva = Electiva.objects.create(name=name,password=password)
    
            return redirect('login')

def tablaHorario(request):
    
    if request.method == 'POST':
        name=request.POST.get('username')
        password = request.POST.get('password')
        try:
            electiva = Electiva.objects.get(name=name,password=password)
            context = {'electiva': electiva}
            return render(request,'tablaHorario.html',context=context)
        except:
            
        #electiva = Electiva.objects.create(name=name,password=password)
    
            return redirect('login')
