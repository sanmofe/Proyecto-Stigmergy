from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic import logic_calificacion

# Create your views here.
def get_calificaciones(request):
    calificaciones = logic_calificacion.get_all_calificaciones()
    calificacions_list = serializers.serialize('json', calificaciones)
    return HttpResponse(calificaciones_list, content_type='application/json')

def get_calificacion(request, id):
    calificacion = logic_calificacion.get_calificacion(id)
    calificacion_rta= serializers.serialize('json', calificacion)
    return HttpResponse(calificacion_rta, content_type='application/json')

def delete_calificacion(request, id):
    calificacion = logic_calificacion.delete_calificacion(id)
    calificacion_rta= serializers.serialize('json', calificacion)
    return HttpResponse(calificacion_rta, content_type='application/json')

