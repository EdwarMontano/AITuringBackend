from django.urls import path
# from django.contrib.auth.decorators import login_required
from .views import *
# from .formsets import FormsetAutor

urlpatterns = [
    # path('pagenofound/', pageNoFound, name = 'File404'),
    path('tableClientes/', HomeCliente, name = 'tablecliente'),
    path('graphClientes/', graficasCliente, name = 'graphcliente'),
    path('crearCliente/', crearClienteIndividual, name = 'crearcliente'),
    path('poblarClientes/', crearClienteMasivo , name = 'populationCliente')
    
]
