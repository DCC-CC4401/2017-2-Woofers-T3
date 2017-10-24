from django.contrib.auth import (authenticate,
                                 login, logout)
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import UpdateView

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
        form = FichaAnimalForm(request.POST or None)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            edad = form.cleaned_data['edad']
            tiempo = form.cleaned_data['tiempo']
            denuncia = form.cleaned_data['denuncia']
            ficha = FichaAnimal(nombre=nombre, edad=edad, tiempo=tiempo, denuncia=denuncia)
            ficha.save()

            return redirect('/')
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})


def muni(request):
    lista_denuncias = Denuncia.objects.all()
    context = {'lista_denuncias': lista_denuncias, }
    return render(request, 'municipalidad-denuncias.html', context)


def editdenuncia(request, pk):
    if request.method == 'POST':

        den = Denuncia.objects.get(pk=int(pk))
        form = DenunciaForm(request.POST, instance=den)
        # den.maltrato = form.cleaned_data['maltrato']
        # den.especie = form.cleaned_data['especie']
        # den.sexo = form.cleaned_data['sexo']
        # den.imagen = den.imagen
        # den.direccion = form.cleaned_data['direccion']
        # den.color = form.cleaned_data['color']
        # den.herido = form.cleaned_data['herido']
        # den.comentario = form.cleaned_data['comentario']

        if form.is_valid():
            # den.save()
            form.save()
            # print(form.cleaned_data['maltrato'])

        return redirect('/municipalidad-denuncias')

    else:
        den = Denuncia.objects.get(pk=pk)
        form = DenunciaForm(instance=den)
        return render(request, 'editdenuncia.html', {'form': form, 'ID': pk})


def estadisticasDenuncias(request):
    denuncias = Denuncia.objects.all()
    ##abiertas = Denuncia.objects.filter(estado="Abierta")
    cantidad = len(denuncias)
    abandono = 0
    temperatura = 0
    agua = 0
    comida = 0
    violencia = 0
    venta = 0
    perros = 0
    gatos = 0
    otros = 0
    for denuncia in denuncias:
        if denuncia.especie =="Perro":
            perros+=1
        if denuncia.especie =="Gato":
            perros+=1
        if denuncia.especie =="Otro":
            otros+=1
        if denuncia.maltrato == "Abandono en la calle":
            abandono += 1
        if denuncia.maltrato == "Falta de Agua":
            agua += 1
        if denuncia.maltrato == "Exposición a temperaturas extremas":
            temperatura += 1
        if denuncia.maltrato == "Violencia":
            violencia += 1
        if denuncia.maltrato == "Falta de comida":
            comida += 1
        if denuncia.maltrato == "Venta ambulante":
            venta += 1
    context = {'cantidad': cantidad, 'abandono': abandono, 'temperatura': temperatura, 'agua': agua,
               'comida': comida, 'violencia': violencia, 'venta': venta, 'perros':perros, 'gatos':gatos, 'otros':otros}
    return render(request, 'municipalidad-estadisticas-denuncias.html', context)

def estadisticasONG(request):
    return render(request, "municipalidad-estadisticas-ong.html")

def estadisticasONGONG(request):
    return render(request, "municipalidad-estadisticas-ongs-ong.html")