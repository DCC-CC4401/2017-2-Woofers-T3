from django.contrib.auth import (authenticate,
                                 get_user_model,
                                 login, logout)
from django import forms



class DenunciaForm(forms.Form):

    opcionesMaltrato = (
        ("m1", "Abandono en la calle"),
        ("m2", "Exposición a temperaturas extremas"),
        ("m3", "Falta de agua"),
        ("m4", "Falta de comida"),
        ("m5", "Violencia"),
        ("m6", "Venta ambulante")
    )
    opcionesEspecie = (
        ("e1", "Perro"),
        ("e2", "Gato"),
        ("e3", "Otro")

    )
    opcionesSexo = (
        ("s1", "Macho"),
        ("s2", "Hembra"),
        ("s3", "Desconocido")
    )
    opcionesHerido = (
        ("h1", "Si"),
        ("h2", "No")
    )

    maltrato = forms.TypedChoiceField(widget=forms.Select, choices=opcionesMaltrato)
    especie = forms.TypedChoiceField(widget=forms.Select, choices=opcionesEspecie)
    sexo = forms.TypedChoiceField(widget=forms.RadioSelect, choices=opcionesSexo)
    imagen = forms.ImageField(label="Foto de la Denuncia", widget=forms.FileInput)
    direccion = forms.CharField(label='Dirección', widget=forms.TextInput)
    color = forms.CharField(label='Color', max_length=100)
    herido = forms.TypedChoiceField(widget=forms.RadioSelect, choices=opcionesHerido)
    comentario = forms.CharField(label='Comentario:', widget=forms.Textarea)

class UsuarioForm(forms.Form):

    usuario = forms.CharField(label='Usuario', widget=forms.TextInput)
    correo = forms.EmailField(label='Correo', widget=forms.EmailInput)
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput)
    apellido = forms.CharField(label='Apellido', widget=forms.TextInput)
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    rut = forms.CharField(label='Rut', widget=forms.TextInput)
    imagen = forms.ImageField(label='Foto de Perfil', widget=forms.FileInput)
    telefono = forms.CharField(label='Celular', widget=forms.TextInput)

class UsuarioLoginForm(forms.Form):

    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Usuario', 'class':
        'form-control'}))

    contrasena = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña',
                                                                   'class':'form-control'}))
class FichaAnimalForm(forms.Form):

    opcionesEspecie = (
        ("e1", "Perro"),
        ("e2", "Gato"),
        ("e3", "Otro")
    )
    opcionesSexo = (
        ("s1", "Macho"),
        ("s2", "Hembra"),
        ("s3", "Desconocido")
    )

    nombre = forms.CharField(label='Nombre', widget=forms.TextInput)
    especie = forms.TypedChoiceField(widget=forms.Select, choices=opcionesEspecie)
    sexo = forms.TypedChoiceField(widget=forms.RadioSelect, choices=opcionesSexo)
    edad = forms.CharField(label='Edad', widget=forms.NumberInput)
    tiempo = forms.CharField(label='Tiempo en Adopcion', widget=forms.NumberInput)
    imagen = forms.ImageField(label="Foto de la Denuncia", widget=forms.FileInput)


