from django.db import models
from pedido.models import Pedido

# Create your models here.
class Calificacion(models.Model):
	"""docstring for Calificacion
	"""
	"""
	def __init__(self, arg):
		super(Calificacion
		, self).__init__()
		self.arg = arg
	"""	
	pedido= models.OneToOneField(Pedido, on_delete= models.CASCADE, primary_key=True, default=None)
	comentario =models.CharField(max_length=150)
	estrellas=models.FloatField(null= True, blank=True, default=None)
	sabor =models.CharField(max_length=150)
	
	def __str__(self):
		return '%s %s' % (self.comentario, self.estrellas)
		return '{}'.format(self.sabor)
