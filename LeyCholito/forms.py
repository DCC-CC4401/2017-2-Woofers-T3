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
    color = forms.CharField(label='Color', max_length=100)
    herido = forms.TypedChoiceField(widget=forms.RadioSelect, choices=opcionesHerido)


class UsuarioForm(forms.Form):

    correo = forms.EmailField(label='Correo', widget=forms.EmailInput)
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput)
    rut = forms.CharField(label='Rut', widget=forms.TextInput)
    #imagen = forms.ImageField(label='Foto de Perfil', widget=forms.FileInput)
    telefono = forms.CharField(label='Celular', widget=forms.TextInput)


