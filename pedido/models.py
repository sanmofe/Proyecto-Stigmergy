from django.db import models
from django.utils.translation import gettext_lazy as _
from hub.models import Hub
from comprador.models import Comprador

# Create your models here.

class Pedido(models.Model):
    class Estado(models.TextChoices):
        ORDENADO        = 'OR', _("Ordenado")
        CANCELADO       = 'CN', _("Cancelado")
        EN_PREPARACION  = 'EP', _("En preparación")
        EN_HUB_1        = 'H1', _("En hub de salida")
        VOLANDO         = 'VL', _("Volando")
        EN_HUB_2        = 'H2', _("En hub de entrega")
        ENTREGADO       = 'EN', _("Entregado")

    hub = models.ForeignKey(Hub, on_delete= models.CASCADE, default= None)
    comprador = models.ForeignKey(Comprador, on_delete= models.CASCADE, default= None)
    direccion = models.CharField(max_length=50)
    dateTime = models.DateTimeField()
    precio = models.FloatField(null=True, blank=True, default=None)
    estado = models.CharField(
        max_length=2,
        choices = Estado.choices,
        default = Estado.EN_PREPARACION,
    )

    def __str__(self):
        return '%s %s' % (self.estado, self.dateTime, self.direccion)
