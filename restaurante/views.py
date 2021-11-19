from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, request
from django.core import serializers
from .logic import logic_restaurante
from django.contrib import messages
from .forms import RestauranteForm
from Stygmergy.auth0_backend import getRole 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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

@csrf_exempt
def create_restaurante(request):
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
        
@login_required
def restaurante_create(request):
    role = getRole()
    if role == "restaurante" or role == "admin":
        if request.method == 'POST':
            form = RestauranteForm(request.POST)
            if form.is_valid():
                create_restaurante(form)
                messages.add_message(request, messages.SUCCESS, 'Succesfully created a restaurant')
                return HttpResponseRedirect(reverse('restauranteCreate'))
            else:
                print(form.errors)
        else:
            form = RestauranteForm()
        
        context = {
            'form' : form,
        }
        return render(request, 'restaurante/list', context)
    else:
        return HttpResponse("Unauthorized User")