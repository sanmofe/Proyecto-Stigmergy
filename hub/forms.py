from django import forms
from .models import Hub

class HubForm(forms.ModelForm):
    class Meta:
        model = Hub
        fields = [
            'direccion',
            'restaurante'
        ]

        labels = {
            'direccion' : 'Dirección',
            'restaurante' : 'Restaurante',
        }