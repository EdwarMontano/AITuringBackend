import csv
import json

from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    TemplateView,
    UpdateView,
)

from .models import Cliente

from cliente.forms import ClienteForm
from utils.population import poblarMasivo

# from .population import *


class ListadoCliente(TemplateView):
    model = Cliente
    template_name = "tables.html"
    # context_object_name = 'clientes'
    # queryset= Cliente.objects.filter(estado=True)

    # import pdb; pdb.set_trace()
    # def get_queryset(self):
    #     return self.model.objects.filter(estado=True)

    def get(self, request, *args, **kwargs):
        clientesjson = json.loads(
            serialize(
                "json", Cliente.objects.filter(estado=True), use_natural_foreign_keys=True
            )
        )

        return render(request, self.template_name, {"clientesjson": clientesjson})
        # if is_ajax(request=request):
        # else:
        #     return redirect('cliente:listarCliente')


class EditarCliente(UpdateView):
    model = Cliente
    template_name = "crearCliente.html"
    form_class = ClienteForm
    success_url = reverse_lazy("cliente:listarCliente")


class CrearCliente(CreateView):
    model = Cliente
    template_name = "crearCliente.html"
    form_class = ClienteForm
    success_url = reverse_lazy("cliente:listarCliente")


class EliminarCliente(DeleteView):
    model = Cliente

    def post(self, request, pk, *args, **kwargs):
        object = Cliente.objects.get(pk=pk)
        object.estado = False
        object.save()
        return redirect("cliente:listarCliente")


class ExportCliente(TemplateView):
    model = Cliente
    template_name = "exportCliente.html"


@login_required
def exportDataAllCliente(request):
    clientesjson = json.loads(
        serialize(
            "json", Cliente.objects.filter(estado=True), use_natural_foreign_keys=True
        )
    )
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(["pk", "nombre de cliente", "categoria", "pais", "city", "estado"])

    for fila in clientesjson:
        texto = [
            str(fila["pk"]),
            fila["fields"]["name_cliente"],
            fila["fields"]["categoria"],
            fila["fields"]["pais"],
            fila["fields"]["city"],
            str(fila["fields"]["estado"]),
        ]
        # import pdb; pdb.set_trace()
        writer.writerow(texto)
    response["Content-Disposition"] = 'attachment; filename="clientes.csv"'

    return response


@login_required
def exportDataCountryColombia(request):
    clientesjson = json.loads(
        serialize("json", Cliente.objects.filter(pais="1"), use_natural_foreign_keys=True)
    )
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(["pk", "nombre de cliente", "categoria", "pais", "city", "estado"])

    for fila in clientesjson:
        texto = [
            str(fila["pk"]),
            fila["fields"]["name_cliente"],
            fila["fields"]["categoria"],
            fila["fields"]["pais"],
            fila["fields"]["city"],
            str(fila["fields"]["estado"]),
        ]
        # import pdb; pdb.set_trace()
        writer.writerow(texto)
    response["Content-Disposition"] = 'attachment; filename="clientesColombia.csv"'

    return response


@login_required
def exportDataCountryMexico(request):
    clientesjson = json.loads(
        serialize("json", Cliente.objects.filter(pais="2"), use_natural_foreign_keys=True)
    )
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(["pk", "nombre de cliente", "categoria", "pais", "city", "estado"])

    for fila in clientesjson:
        texto = [
            str(fila["pk"]),
            fila["fields"]["name_cliente"],
            fila["fields"]["categoria"],
            fila["fields"]["pais"],
            fila["fields"]["city"],
            str(fila["fields"]["estado"]),
        ]
        # import pdb; pdb.set_trace()
        writer.writerow(texto)
    response["Content-Disposition"] = 'attachment; filename="clientesMexico.csv"'

    return response


@login_required
def exportDataCountryVenezuela(request):
    clientesjson = json.loads(
        serialize("json", Cliente.objects.filter(pais="3"), use_natural_foreign_keys=True)
    )
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(["pk", "nombre de cliente", "categoria", "pais", "city", "estado"])

    for fila in clientesjson:
        texto = [
            str(fila["pk"]),
            fila["fields"]["name_cliente"],
            fila["fields"]["categoria"],
            fila["fields"]["pais"],
            fila["fields"]["city"],
            str(fila["fields"]["estado"]),
        ]
        # import pdb; pdb.set_trace()
        writer.writerow(texto)
    response["Content-Disposition"] = 'attachment; filename="clientesVenezuela.csv"'

    return response


def graficasCliente(request):
    return render(request, "charts.html")


def crearClienteMasivo(request):
    if request.method == "GET":
        num_clientes = int(request.GET["cantidad"])
        response_masivo = poblarMasivo(num_clientes)
        print("Voy 4")
        print("SOy response;", response_masivo)
        return render(
            request, "cliente_Masivo.html", {"response_masivo": response_masivo}
        )


def crearClienteIndividual(request):
    if request.method == "POST":
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect("index")
    else:
        cliente_form = ClienteForm()
    return render(request, "crearCliente.html", {"cliente_form": cliente_form})


# def listarcliente(request):
#     clientes=Cliente.objects.all()
#     # import pdb; pdb.set_trace()
#     return render(request,'tables.html',{'clientes':clientes})
