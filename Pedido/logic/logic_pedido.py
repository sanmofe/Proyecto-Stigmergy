# -*- coding: utf-8 -*-
"""
Created on Fri Oct 1 02:20:02 2021

@author: Miguel
"""

from ..models import Pedido

def get_all_pedido():
    pedidos = Pedido.objects.all()
    return pedidos
