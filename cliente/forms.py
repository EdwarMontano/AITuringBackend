from django import forms
from .models import Category,Cliente,Pais

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['name_cliente','categoria','pais','city']
