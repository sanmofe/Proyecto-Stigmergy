from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .logic import logic_hub
from .forms import HubForm

# Create your views here.
@csrf_exempt
def create_comprador(request):
    if request.method == 'POST':
        form = HubForm(request.POST)
        if form.is_valid():
            logic_hub.create_pedido(form)
            messages.add_message(request, messages.SUCCESS, 'Pedido creado exitosamente')
        else:
            print(form.errors)
    else:
        form = HubForm()
    return render(request, 'create_pedido.html', {'form':form})
