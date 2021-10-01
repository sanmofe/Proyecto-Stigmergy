from ..models import Restaurante

def get_all_restaurantes():
    restaurantes = restaurante.objects.all()
    return restaurantes

def get_restaurante(identificador: int):
    restaurante= restaurante.objects.filter(pk= identificador)
    return restaurante

def delete_restaurante(identificador: int):
    restaurante= get_restaurante(identificador)
    restaurante.delete()
    return restaurante