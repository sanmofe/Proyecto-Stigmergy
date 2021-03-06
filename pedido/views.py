from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import PedidoForm
from .forms import PedidoForm   
from .logic import logic_pedido
from django.core import serializers
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            logic_pedido.create_pedido(form)
            messages.add_message(request, messages.SUCCESS, 'Pedido creado exitosamente')
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

def update_estadoPedido(request, id):
    pedido = Pedido.objects.get(id = id)
    if request.method == 'GET':
        form = PedidoForm(instance = pedido)
    else: 
        form = PedidoForm(request.POST, instance = pedido)
        form.save()
        return redirect('list_pedido')

    return render(request, 'editPedido.html', {'form':form})