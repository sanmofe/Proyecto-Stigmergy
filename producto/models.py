from django.db import models
from restaurante.models import Restaurante
from pedido.models import Pedido
# Create your models here.
class Producto(models.Model):
	"""docstring for Producto"""
	"""
	def __init__(self, arg):
		super(Producto, self).__init__()
		self.arg = arg
	"""
	restaurante = models.ForeignKey(Restaurante, on_delete= models.CASCADE, default= None)
	pedido= models.ForeignKey(Pedido, on_delete= models.CASCADE, default= None, null= True, blank=True)
	nombre =models.CharField(max_length=50)
	precio =models.FloatField(null= True, blank=True, default=None)
	informacion=models.CharField(max_length=150)

	def __str__(self):
		return '%s %s' % (self.nombre, self.precio)
		return '{}'.format(self.informacion)
