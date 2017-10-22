from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^felicidades$', )
    # url(r'^ingresado$', login, {'template_name':'ingresado.html'}, name='login'),
    url(r'^salir$', views.cerrar_sesion, name='salir'),
    url(r'^ingresado$', views.ingresado, name='ingresado'),
    url(r'^fichaAnimal$', views.fichaAnimal, name='fichaAnimal'),
    url(r'^registro$', views.registro, name='registro'),
    url(r'^ingreso$', views.ingreso, name='ingreso'),
    url(r'^denuncia$', views.denuncia, name='denuncia'),
    url(r'^muni$', views.muni, name='muni'),
    url(r'^editdenuncia/(?P<IDdenuncia>[0-9]+)/', views.editdenuncia, name='editdenuncia'),
    url(r'$', views.index, name='index'),
]
