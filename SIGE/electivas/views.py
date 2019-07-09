from django.shortcuts import render
from django.views.generic import ListView
from .models import Electiva
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.


class ElectivaList(ListView):
    model = Electiva

class ElectivaDetail(DetailView):
    model = Electiva

class ElectivaCreation(CreateView):
    model = Electiva
    success_url = reverse_lazy('electivas:list')
    fields = ['name', 'start_date', 'end_date', 'picture']

class ElectivaUpdate(UpdateView):
    model = Electiva
    success_url = reverse_lazy('electivas:list')
    fields = ['name', 'start_date', 'end_date', 'picture']

class ElectivaDelete(DeleteView):
    model = Electiva
    success_url = reverse_lazy('electivas:list')
