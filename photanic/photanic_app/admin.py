from django.contrib import admin

from . import models

admin.site.register(models.Usuario)
admin.site.register(models.Planta)
admin.site.register(models.Foto)
admin.site.register(models.Comentario)
admin.site.register(models.Articulo)
admin.site.register(models.Valoracion)
# Register your models here.
