import json

from time import time
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import ClienteForm


# Create your views here.
def HomeCliente(request):    
    return render(request,'tables.html')

def graficasCliente(request):    
    return render(request,'charts.html')

def crearClienteMasivo(request):    
    return render(request,'blank.html')

def crearClienteIndividual(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()            
            return redirect('index')
    else:
        cliente_form = ClienteForm()            
    return render(request,'crearCliente.html',{'cliente_form':cliente_form})


