from django import forms
from .models import Restaurante

class HubForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = [
            'nombre',
            'clave',
            'cuenta', #Cuenta bancaria
            'direccion'
        ]

        labels = {
            'nombre' : 'Nombre',
            'clave' : 'Clave',
            'cuenta' : 'Cuenta',
            'direccion' : 'Dirección',
        }