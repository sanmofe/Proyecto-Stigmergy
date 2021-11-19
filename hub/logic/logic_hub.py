from ..models import Hub

def get_all_hubs():
    hubs = Hub.objects.all()
    return hubs

def get_hub(identificador: int):
    hub = Hub.objects.filter(pk= identificador)
    return hub

def delete_hub(identificador: int):
    hubDel= get_hub(identificador)
    hubDel.delete()
    return hubDel

def create_hub(form):
    hub = form.save()
    hub.save()
    return()