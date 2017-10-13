from django.contrib import admin

from .models import Denuncia, UserInfo

admin.site.register(UserInfo)
admin.site.register(Denuncia)