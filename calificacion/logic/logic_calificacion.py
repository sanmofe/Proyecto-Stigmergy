from ..models import Calificacion

def get_all_calificaciones():
    calificacions = Calificacion.objects.all()
    return calificacions

def get_calificacion(identificador: int):
    calificacion= Calificacion.objects.filter(pk= identificador)
    return calificacion

def delete_calificacion(identificador: int):
    calificaciSon= get_calificacion(identificador)
    calificacion.delete()
    return calificacion