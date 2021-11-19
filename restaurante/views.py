from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic import logic_restaurante
from django.contrib import messages
from .forms import RestauranteForm

# Create your views here.
def get_resturantes(request):
    resturantes = logic_restaurante.get_all_resturantes()
    resturantes_list = serializers.serialize('json', resturantes)
    return HttpResponse(resturantes_list, content_type='application/json')

def get_resturante(request, id):
    resturante = logic_restaurante.get_resturante(id)
    resturante_rta= serializers.serialize('json', resturante)
    return HttpResponse(resturante_rta, content_type='application/json')

def delete_resturante(request, id):
    resturante = logic_restaurante.delete_resturante(id)
    resturante_rta= serializers.serialize('json', resturante)
    return HttpResponse(resturante_rta, content_type='application/json')


def create_restaurante(request, id):
    if request.method == 'POST':
        form = RestauranteForm(request.POST)
        if form.is_valid():
            logic_restaurante.create_restaurante(form)
            messages.add_message(request, messages.SUCCESS, 'Restaurante creado')
        else:
            print(form.errors)
    else:
        form = RestauranteForm()
    return render(request, 'create_pedido.html', {'form':form})
        
        