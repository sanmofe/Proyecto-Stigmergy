from ..models import Dron

def get_all_drons():
    dron = Dron.objects.all()
    return dron

def get_dron(identificador: int):
    dron = Dron.objects.filter(pk= identificador)
    return dron

def delete_dron(identificador: int):
    dronDel= get_dron(identificador)
    dronDel.delete()
    return dronDel