from django.contrib.auth.models import User
from django.db import models

class Denuncia(models.Model):

    ID = models.AutoField(primary_key=True, unique=True)
    maltrato = models.CharField(max_length=20)
    especie = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10)
    imagen = models.FileField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=10)
    herido = models.CharField(max_length=2)
    comentario = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return "%s %s" % (self.maltrato, self.direccion)

'''Usaremos una relacion many-to-one para usar la info de las denuncias en las ficha animal'''
class UserInfo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    rut = models.CharField(max_length=20)
    imagen = models.FileField(null=True, blank=True)
    telefono = models.CharField(max_length=20)
    isMuniAdmin = models.BooleanField(default=False)

    '''def __str__(self):
        return self.usuario

    @staticmethod
    def obtener_usuarios():
        consulta = Usuario.objects.all()
        usuarios = [usuario for usuario in consulta]
        return usuarios

    @staticmethod
    def obtener_datos():
        consulta = Usuario.obtener_usuarios()
        datos = {}
        for dato in consulta:
            datos[dato.correo] = dato.contrasena
        return datos
    '''

'''Usaremos una relacion many-to-one para usar la info de las denuncias en las ficha animal'''
class FichaAnimal(models.Model):

    nombre = models.CharField(max_length=20)
    edad = models.CharField(max_length=20)
    tiempo = models.CharField(max_length=20)
    denuncia = models.OneToOneField(Denuncia, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return self.nombre