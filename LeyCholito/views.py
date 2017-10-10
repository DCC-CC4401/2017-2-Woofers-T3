from django.shortcuts import render, redirect

from .forms import DenunciaForm, UsuarioForm
from .models import Denuncia, Usuario


def index(request):

    return render(request, 'index.html')

def formulario(request):

    if request.method == 'POST':

        form = DenunciaForm(request.POST or None)

    else:
        form = DenunciaForm()


    return render(request, 'denuncia.html', {'form': form})




def registro(request):

    if request.method == 'POST':

        form = UsuarioForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']
            nombre = form.cleaned_data['nombre']
            rut = form.cleaned_data['rut']
            #imagen = form.cleaned_data['imagen']
            telefono = form.cleaned_data['telefono']
            usuario = Usuario(correo=correo, contrasena=contrasena, nombre=nombre, rut=rut,
                              telefono=telefono)
            usuario.save()

            return redirect('/index/')
    else:

        form = UsuarioForm()
    return render(request, 'registro.html', {'form':form})

def ingreso(request):
    return render(request, 'ingreso.html', {'ingreso': ingreso})
