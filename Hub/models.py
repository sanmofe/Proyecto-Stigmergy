from django.db import models
from restaurante.models import Restaurante

# Create your models here.

class Hub(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete= models.CASCADE, default= None)
    direcccion = models.CharField(max_length=150)


    def __str__(self):
        return '%s' % (self.direcccion)
