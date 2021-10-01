from django.shortcuts import render, redirect

from .models import *
from .logic import logic_pedido
from django.core import serializers
from django.http import HttpResponse
import json

# Create your views here.

def list_pedido(request):
    pedidos = logic_pedido.get_all_pedido()
    pedido_list = serializers.serialize('json',pedidos)
    pedido_list = json.loads(pedido_list)
    return render(request, 'list_pedido.html', {'pedidos':pedido_list})
