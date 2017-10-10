
from django.db import models

class Denuncia(models.Model):

    maltrato = models.CharField(max_length=20)
    especie = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    herido = models.CharField(max_length=2)

class Usuario(models.Model):

    correo = models.EmailField(max_length=20)
    contrasena = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=20)
    imagen = models.FileField(null=True, blank=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
