from django.contrib import admin
from django.contrib.auth.admin import User
from . import models
from .models import *

admin.site.register(User)
admin.site.register(Planta)
admin.site.register(Foto)
admin.site.register(Comentario)
admin.site.register(Articulo)
admin.site.register(Valoracion)