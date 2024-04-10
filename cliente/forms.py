from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["name_cliente", "categoria", "pais", "city"]
        labels = {
            "name_cliente": "Nombre de Cliente",
            "categoria": "Categoría",
            "pais": "País",
            "city": "Ciudad",
        }
        widgets = {
            "name_cliente": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del Cliente",
                }
            ),
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "pais": forms.Select(attrs={"class": "form-control"}),
            "city": forms.Select(attrs={"class": "form-control"}),
        }
