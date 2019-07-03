from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users
from django.contrib.auth import authenticate, login

# Create your views here.


def login(request):
    users = Users.objects.all()
    context = {'user': users}
    
    return render(request,'IniciarSesion.html',context=context)
'''
def index(request):
    
    if request.method == 'POST':
        name=request.POST.get('username')
        password = request.POST.get('password')
        try:
            users = Users.objects.get(name=name,password=password)
            context = {'user': users}
            return render(request,'index.html',context=context)
        except:
            
        #electiva = Electiva.objects.create(name=name,password=password)
    
            return redirect('login')
'''

def tablaHorario(request):
    
    if request.method == 'POST':
        name=request.POST.get('username')
        password = request.POST.get('password')
        try:
            users = Users.objects.get(name=name,password=password)
            context = {'electiva': users}
            return render(request,'tablaHorario.html',context=context)
        except:
            
        #electiva = Electiva.objects.create(name=name,password=password)
    
            return redirect('login')
    else:
        now = "Ahorita"
        html = "<html><link rel='stylesheet' href='blog-post.css'/><body><div class='rojo'>It is now %s.</div></body></html>" % now
        return HttpResponse(html)
        