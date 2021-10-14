# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 05:57:57 2021

@author: miguel
"""

from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'hub',
            'comprador',
            'direccion',
            'dateTime',
            'precio',
            'estado'
        ]

        labels = {
            'hub' : 'Hub',
            'comprador' : 'Comprador',
            'direccion' : 'Dirección',
            'dateTime' : 'Date Time',
            'precio' : 'Precio',
            'estado' : 'Estado',
        }
