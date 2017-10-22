from django import forms

from .models import Denuncia


class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields='__all__'

    opcionesMaltrato = (
        ("Abandono en la calle", "Abandono en la calle"),
        ("Exposición a temperaturas extremas", "Exposición a temperaturas extremas"),
        ("Falta de agua", "Falta de agua"),
        ("Falta de comida", "Falta de comida"),
        ("Violencia", "Violencia"),
        ("Venta ambulante", "Venta ambulante")
    )
    opcionesEspecie = (
        ("Perro", "Perro"),
        ("Gato", "Gato"),
        ("Otro", "Otro")

    )
    opcionesSexo = (
        ("M", "Macho"),
        ("F", "Hembra"),
        ("Desconocido", "Desconocido")
    )
    opcionesHerido = (
        ("Si", "Si"),
        ("No", "No")
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
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class':
        'form-control'}))

    contrasena = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña',
                                                                   'class': 'form-control'}))


class FichaAnimalForm(DenunciaForm):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput)
    edad = forms.CharField(label='Edad', widget=forms.NumberInput)
    tiempo = forms.CharField(label='Tiempo en Adopcion', widget=forms.NumberInput)
    denuncia = forms.ModelChoiceField(label='Denuncia', queryset=Denuncia.objects.all())
