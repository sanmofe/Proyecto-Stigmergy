from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    clave = models.CharField(null=False, default=None, blank=False)

    def __str__(self):
        return '%s %s' % (self.nombre, self.clave)
