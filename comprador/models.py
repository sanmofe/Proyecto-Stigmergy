from django.db import models

# Create your models here.
class Comprador(models.Model):
	"""docstring for Comprador"""
	"""def __init__(self, arg):
		super(Comprador, self).__init__()
		self.arg = arg
	"""
	nombre=models.CharField(max_length=50) 
	clave=models.CharField(max_length=50)
	telefono=models.CharField(max_length=50)

	def __str__(self):
		return '%s %s' % (self.telefono, self.nombre)
		return '{}'.format(self.nombre)
