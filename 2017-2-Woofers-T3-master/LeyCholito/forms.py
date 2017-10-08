from django import forms

class DenunciaForm(forms.Form):
    opciones = (
        ("m1", "Abandono en la calle"),
        ("m2", "Exposición a temperaturas extremas"),
        ("m3", "Falta de agua"),
        ("m4", "Falta de comida"),
        ("m5", "Violencia"),
        ("m6", "Venta ambulante")
    )

    maltrato = forms.TypedChoiceField(widget=forms.Select, choices=opciones)