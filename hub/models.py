from django.db import models

# Create your models here.

class Hub(models.Model):
    direcccion = models.CharField(max_length=150)


    def __str__(self):
        return '%s' % (self.direcccion)
