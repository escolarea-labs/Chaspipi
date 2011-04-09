from django.db import models

class Lista(models.Model):
    codigo = models.TextField(max_length=10)
    titulo = models.TextField(null=True, blank=True, default='')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_acceso = models.DateTimeField(auto_now=True)

