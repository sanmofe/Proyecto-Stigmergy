from ..models import Calificacion

def get_all_calificaciones():
    calificacions = calificacion.objects.all()
    return calificacions

def get_calificacion(identificador: int):
    calificacion= calificacion.objects.filter(pk= identificador)
    return calificacion

def delete_calificacion(identificador: int):
    calificacion= get_calificacion(identificador)
    calificacion.delete()
    return calificacion