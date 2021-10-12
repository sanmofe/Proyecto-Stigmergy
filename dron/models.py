from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Dron(models.Model):
    bateria= models.FloatField(null=False, blank=False, default=0)
    serial = CharField(null=False, blank=False, max_length=100)
