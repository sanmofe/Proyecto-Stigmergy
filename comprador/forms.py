from django import forms
from .models import Comprador

class CompradorForm(forms.ModelForm):
    class Meta:
        model = Comprador
        fields = [
            'nombre',
            'clave',
            'telefono'
        ]

        labels = {
            'nombre' : 'Nombre',
            'clave' : 'Clave',
            'telefono' : 'Telefono',
        }