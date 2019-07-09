from django.shortcuts import render
 
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Postres' para poder usarlo en nuestras Vistas CRUD
from .models import Electiva
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms



class ElectivaListado(ListView):
    model = Electiva

class ElectivaDetalle(DetailView): 
    model = Electiva

class ElectivaCrear(SuccessMessageMixin, CreateView): 
    model = Electiva 
    form = Electiva 
    fields = "__all__"
    success_message = 'Electiva Creado Correctamente !' 
     
    def get_success_url(self):        
        return reverse('leer') 

class ElectivaActualizar(SuccessMessageMixin, UpdateView): 
    model = Electiva 
    form = Electiva 
    fields = "__all__" 
    success_message = 'Electiva Actualizado Correctamente !' 
     
    def get_success_url(self):               
        return reverse('leer')

class ElectivaEliminar(SuccessMessageMixin, DeleteView): 
    model = Electiva 
    form = Electiva
    fields = "__all__"     
     
    def get_success_url(self): 
        success_message = 'Electiva Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer')
