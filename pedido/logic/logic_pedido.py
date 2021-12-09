# -*- coding: utf-8 -*-
"""
Created on Fri Oct 1 02:20:02 2021

@author: Miguel
"""

from ..models import Pedido

def get_all_pedido():
    pedidos = Pedido.objects.all()
    return pedidos

def get_pedido(identificador):
    pedido = Pedido.objects.get(id = identificador)
    return pedido

def create_pedido(form):
    pedido = form.save()
    pedido.save()
    return()

def update_pedido(identificador: int, newState):
    pedido= Pedido.objects.get(id = identificador)
    pedido.update(newState)
    return pedido
