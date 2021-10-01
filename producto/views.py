from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic import logic_producto

# Create your views here.
def get_productos(request):
    productos = logic_producto.get_all_productos()
    productos_list = serializers.serialize('json', productos)
    return HttpResponse(productos_list, content_type='application/json')

def get_producto(request, id):
    producto = logic_producto.get_producto(id)
    producto_rta= serializers.serialize('json', producto)
    return HttpResponse(producto_rta, content_type='application/json')

def delete_producto(request, id):
    producto = logic_producto.delete_producto(id)
    producto_rta= serializers.serialize('json', producto)
    return HttpResponse(producto_rta, content_type='application/json')
