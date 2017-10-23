from django.conf.urls import url

from . import views
from .views import EditDenunciaView

urlpatterns = [
    # url(r'^felicidades$', )
    # url(r'^ingresado$', login, {'template_name':'ingresado.html'}, name='login'),
    url(r'^salir$', views.cerrar_sesion, name='salir'),
    url(r'^ingresado$', views.ingresado, name='ingresado'),
    url(r'^fichaAnimal$', views.fichaAnimal, name='fichaAnimal'),
    url(r'^registro$', views.registro, name='registro'),
    url(r'^ingreso$', views.ingreso, name='ingreso'),
    url(r'^denuncia$', views.denuncia, name='denuncia'),
    url(r'^municipalidad-denuncias$', views.muni, name='muni'),
    url(r'^municipalidad-estadisticas-denuncias$', views.estadisticasDenuncias, name='estadisticasDenuncias'),
    url(r'^editdenuncia/(?P<pk>[0-9]*)/', views.editdenuncia, name='editdenuncia'),
    url(r'$', views.index, name='index'),
]
