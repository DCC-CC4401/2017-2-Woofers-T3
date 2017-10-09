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
        ("m1", "Perro"),
        ("m2", "Gato"),
        ("m3", "Otro")
    )
    opcionesSexo = (
        ("m1", "Macho"),
        ("m2", "Hembra"),
        ("m3", "Desconocido")
    )
    opcionesHerido = (
        ("m1", "Si"),
        ("m2", "No")
    )

    maltrato = forms.TypedChoiceField(widget=forms.Select, choices=opcionesMaltrato)
    especie = forms.TypedChoiceField(widget=forms.Select, choices=opcionesEspecie)
    sexo = forms.TypedChoiceField(widget=forms.RadioSelect, choices=opcionesSexo)
    color = forms.CharField(label='Color', max_length=100)
    herido = forms.TypedChoiceField(widget=forms.RadioSelect, choices=opcionesHerido)
