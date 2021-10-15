from ..models import Producto

def get_all_productos():
    productos = Producto.objects.all()
    return productos

def get_producto(identificador: int):
    producto= Producto.objects.filter(pk= identificador)
    return producto

def delete_producto(identificador: int):
    producto= get_producto(identificador)
    producto.delete()
    return producto

def update_producto(identificador: int, idPedido):
	producto= get_producto(identificador)
	producto.update( pedido= idPedido)
	return producto