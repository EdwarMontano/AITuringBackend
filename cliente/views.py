import json
from time import time

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import View,TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from cliente.forms import ClienteForm
from .models import *



class ListadoCliente(ListView):
    model = Cliente
    template_name ='tables.html'
    context_object_name = 'clientes'
    queryset= Cliente.objects.filter(estado=True)


class EditarCliente(UpdateView):
    model = Cliente
    template_name ='crearCliente.html'
    form_class= ClienteForm
    success_url = reverse_lazy('cliente:listarCliente')

class CrearCliente(CreateView):
    model = Cliente
    template_name ='crearCliente.html'
    form_class= ClienteForm
    success_url = reverse_lazy('cliente:listarCliente')

class EliminarCliente(DeleteView):
    model = Cliente       
    
    def post(self,request,pk,*args,**kwargs):
        object = Cliente.objects.get(pk=pk)
        object.estado = False
        object.save()
        return redirect('cliente:listarCliente')



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



# def listarcliente(request):    
#     clientes=Cliente.objects.all()    
#     # import pdb; pdb.set_trace()
#     return render(request,'tables.html',{'clientes':clientes})


