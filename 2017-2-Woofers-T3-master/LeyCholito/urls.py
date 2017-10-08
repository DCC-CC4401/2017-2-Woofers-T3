from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ingreso$', views.ingreso, name='ingreso'),
    url(r'^denuncia$', views.formulario, name='denuncia'),
    url(r'$', views.index, name='index'),
]