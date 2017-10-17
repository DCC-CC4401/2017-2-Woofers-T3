from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    #url(r'^felicidades$', )
    #url(r'^ingresado$', login, {'template_name':'ingresado.html'}, name='login'),
    url(r'^salir$', views.cerrar_sesion, name='salir'),
    url(r'^ingresado$', views.ingresado, name='ingresado'),
    url(r'^registro$', views.registro, name='registro'),
    url(r'^ingreso$', views.ingreso, name='ingreso'),
    url(r'^denuncia$', views.denuncia, name='denuncia'),
    url(r'$', views.index, name='index'),
]