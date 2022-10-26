from django.contrib import admin
from django.contrib.auth.admin import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
from .models import *

admin.site.register(Usuario)
admin.site.register(Planta)
admin.site.register(Foto)
admin.site.register(Comentario)
admin.site.register(Articulo)
admin.site.register(Valoracion)

class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete= False
    verbose_name_plural = 'usuario'
# Register your models here.

class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)