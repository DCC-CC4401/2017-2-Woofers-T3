from django.shortcuts import render

from .forms import DenunciaForm

# Create your views here.

def index(request):

    return render(request, 'index.html')

def formulario(request):


    form = DenunciaForm(request.POST)
    return render(request, 'denuncia.html', {'form': form})

def ingreso(request):
    return render(request, 'ingreso.html', {'ingreso': ingreso})
