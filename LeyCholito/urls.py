from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^felicidades$', )
    url(r'^registro$', views.registro, name='registro'),
    url(r'^ingreso$', views.ingreso, name='ingreso'),
    url(r'^denuncia$', views.denuncia, name='denuncia'),
    url(r'$', views.index, name='index'),
]