from django.shortcuts import render, redirect

from .forms import DenunciaForm, UsuarioForm, UsuarioLoginForm
from .models import Denuncia, Usuario


def index(request):

    return render(request, 'index.html')

def denuncia(request):

    if request.method == 'POST':

        form = DenunciaForm(request.POST or None, request.FILES)
        if form.is_valid():
            maltrato = form.cleaned_data['maltrato']
            especie = form.cleaned_data['especie']
            sexo = form.cleaned_data['sexo']
            imagen = form.cleaned_data['imagen']
            direccion = form.cleaned_data['direccion']
            color = form.cleaned_data['color']
            herido = form.cleaned_data['herido']
            comentario = form.cleaned_data['comentario']
            denuncia = Denuncia(maltrato=maltrato, especie=especie, sexo=sexo, imagen=imagen,
                                direccion=direccion, color=color, herido=herido,
                                comentario=comentario)
            denuncia.save()
            return redirect('/index/')

    else:
        form = DenunciaForm()


    return render(request, 'denuncia.html', {'form': form})




def registro(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']
            nombre = form.cleaned_data['nombre']
            rut = form.cleaned_data['rut']
            imagen = form.cleaned_data['imagen']
            telefono = form.cleaned_data['telefono']
            usuario = Usuario(correo=correo, contrasena=contrasena, nombre=nombre, rut=rut,
                              imagen=imagen, telefono=telefono)
            usuario.save()

            return redirect('/')
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form':form})

def ingreso(request):

    if request.method == 'POST':
        form = UsuarioLoginForm()
    else:
        form = UsuarioLoginForm()


    return render(request, 'ingreso.html', {'form': form})