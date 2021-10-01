from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic import logic_comprador

# Create your views here.
def get_compradores(request):
    compradores = logic_comprador.get_all_compradores()
    compradors_list = serializers.serialize('json', compradores)
    return HttpResponse(compradores_list, content_type='application/json')

def get_comprador(request, id):
    comprador = logic_comprador.get_comprador(id)
    comprador_rta= serializers.serialize('json', comprador)
    return HttpResponse(comprador_rta, content_type='application/json')

def delete_comprador(request, id):
    comprador = logic_comprador.delete_comprador(id)
    comprador_rta= serializers.serialize('json', comprador)
    return HttpResponse(comprador_rta, content_type='application/json')
