from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic import logic_comprador
from .forms import CompradorForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_compradores(request):
    compradores = logic_comprador.get_all_compradores()
    compradors_list = serializers.serialize('json', compradores)
    return HttpResponse(compradors_list, content_type='application/json')

def get_comprador(request, id):
    comprador = logic_comprador.get_comprador(id)
    comprador_rta= serializers.serialize('json', comprador)
    return HttpResponse(comprador_rta, content_type='application/json')

def delete_comprador(request, id):
    comprador = logic_comprador.delete_comprador(id)
    comprador_rta= serializers.serialize('json', comprador)
    return HttpResponse(comprador_rta, content_type='application/json')

@csrf_exempt
def create_comprador(request):
    if request.method == 'POST':
        form = CompradorForm(request.POST)
        if form.is_valid():
            logic_comprador.create_pedido(form)
            messages.add_message(request, messages.SUCCESS, 'Pedido creado exitosamente')
        else:
            print(form.errors)
    else:
        form = CompradorForm()
    return render(request, 'create_pedido.html', {'form':form})
