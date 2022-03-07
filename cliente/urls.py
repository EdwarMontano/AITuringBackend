from django.urls import path
from .views import * 
from django.contrib.auth.decorators import login_required
# from .formsets import FormsetAutor

urlpatterns = [
    # path('pagenofound/', pageNoFound, name = 'File404'),
    # path('login/',Inicio.as_view(), name = 'login'),
    path('listado/',  login_required(ListadoCliente.as_view()) , name = 'listarCliente'),
    path('crearCliente/',   login_required(CrearCliente.as_view()), name = 'crearcliente'),
    path('editarCliente/<int:pk>',  login_required(EditarCliente.as_view()), name = 'editarCliente'),
    path('eliminarCliente/<int:pk>',  login_required(EliminarCliente.as_view()) , name = 'eliminarCliente'),

    path('graphClientes/',  graficasCliente, name = 'graphcliente'),
    path('poblarClientes/', crearClienteMasivo , name = 'populationCliente'),
    path('exportClientes/', exportDataAllCliente , name = 'export')
    
] 