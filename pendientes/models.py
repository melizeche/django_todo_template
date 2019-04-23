from django.db import models

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.BooleanField(default=False)
