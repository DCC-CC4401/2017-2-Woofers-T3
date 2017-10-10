from django.contrib import admin

from .models import Denuncia, Usuario

admin.site.register(Usuario)
admin.site.register(Denuncia)