from ..models import Comprador

def get_all_compradores():
    compradors = comprador.objects.all()
    return compradors

def get_comprador(identificador: int):
    comprador= comprador.objects.filter(pk= identificador)
    return comprador

def delete_comprador(identificador: int):
    comprador= get_comprador(identificador)
    comprador.delete()
    return comprador