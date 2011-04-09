from django.db import models
from lista.models import Lista

class Tarea(models.Model):
    descripcion = models.TextField(max_length=255)
    hecha = models.BooleanField(default=False)
    lista = models.ForeignKey(Lista)

    class Meta:
        ordering=['-id']