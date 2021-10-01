from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic import logic_resturante

# Create your views here.
def get_resturantes(request):
    resturantes = logic_resturante.get_all_resturantes()
    resturantes_list = serializers.serialize('json', resturantes)
    return HttpResponse(resturantes_list, content_type='application/json')

def get_resturante(request, id):
    resturante = logic_resturante.get_resturante(id)
    resturante_rta= serializers.serialize('json', resturante)
    return HttpResponse(resturante_rta, content_type='application/json')

def delete_resturante(request, id):
    resturante = logic_resturante.delete_resturante(id)
    resturante_rta= serializers.serialize('json', resturante)
    return HttpResponse(resturante_rta, content_type='application/json')
