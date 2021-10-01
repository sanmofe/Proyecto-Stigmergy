from django.db import models

# Create your models here.
class Restaurante(models.Model):
	"""docstring for Restaurante"""
	"""
	def __init__(self, arg):
		super(Restaurante, self).__init__()
		self.arg = arg
	"""
	nombre=models.CharField(max_length=50) 
	clave=models.CharField(max_length=50)
	cuenta=models.CharField(max_length=50) #cuenta bancaria
	direccion=models.CharField(max_length=50)

	def __str__(self):
		return '%s %s' % (self.direccions, self.cuenta)
		return '{}'.format(self.nombre)

