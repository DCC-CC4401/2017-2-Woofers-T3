from django.contrib.auth.models import User
from django.contrib.auth import (authenticate,
                                 get_user_model,
                                 login, logout)
from django.shortcuts import render, redirect

from .forms import DenunciaForm, UsuarioForm, UsuarioLoginForm, FichaAnimalForm
from .models import Denuncia, UserInfo, FichaAnimal


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
            usuario = form.cleaned_data['usuario']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']
            rut = form.cleaned_data['rut']
            imagen = form.cleaned_data['imagen']
            telefono = form.cleaned_data['telefono']

            registrar = User.objects.create_user(username=usuario, email=correo,
                                                 password=contrasena)
            registrar.first_name = nombre
            registrar.last_name = apellido
            registrar.save()

            uinfo = UserInfo(usuario=registrar, rut=rut, imagen=imagen, telefono=telefono)
            uinfo.save()

            return redirect('/')
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})


def ingreso(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST or None)
        if form.is_valid():
            nombre = form.cleaned_data['usuario']
            contrasena = form.cleaned_data['contrasena']
            usuario = authenticate(username=nombre, password=contrasena)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'ingresado.html', {})
            else:
                return render(request, 'malingreso.html')



    else:
        form = UsuarioLoginForm()

    return render(request, 'ingreso.html', {'form': form})


def ingresado(request):
    nombre = request.POST['usuario']
    contrasena = request.POST['contrasena']
    usuario = authenticate(username=nombre, password=contrasena)
    if usuario is not None:
        query = User.objects.filter(username=nombre)
        persona = query[0]
        return render(request, 'ingresado.html', {'persona': persona})

    else:
        return render(request, 'malingreso.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('/index/')


def fichaAnimal(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST or None, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            especie = form.cleaned_data['especie']
            sexo = form.cleaned_data['sexo']
            edad = form.cleaned_data['edad']
            tiempo = form.cleaned_data['tiempo']
            imagen = form.cleaned_data['imagen']

            ficha = FichaAnimal(nombre=nombre, especie=especie, sexo=sexo, edad=edad, tiempo=tiempo, imagen=imagen)
            ficha.save()

            return redirect('/')
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})
