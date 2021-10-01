from ..models import Producto

def get_all_productos():
    productos = producto.objects.all()
    return productos

def get_producto(identificador: int):
    producto= producto.objects.filter(pk= identificador)
    return producto

def delete_producto(identificador: int):
    producto= get_producto(identificador)
    producto.delete()
    return producto