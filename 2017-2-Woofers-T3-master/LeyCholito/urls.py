from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^denuncia$', views.formulario, name='denuncia'),
    url(r'$', views.index, name='index'),
]