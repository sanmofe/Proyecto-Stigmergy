from django.shortcuts import render, redirect

from .models import *
from .forms import PedidoForm
from .logic import logic_pedido
from django.core import serializers
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import json

# Create your views here.

def create_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            logic_pedido.create_pedido(form)
            messages.add_message(request, messages.SUCCESS, 'Pedido creado exitosamente')
            return HttpResponseRedirect(reverse('pedidoCreate'))
        else:
            print(form.errors)
    else:
        form = PedidoForm()
    return render(request, 'create_pedido.html', {'form':form})


def list_pedido(request):
    pedidos = logic_pedido.get_all_pedido()
    pedido_list = serializers.serialize('json',pedidos)
    pedido_list = json.loads(pedido_list)
    return render(request, 'list_pedido.html', {'pedidos':pedido_list})
