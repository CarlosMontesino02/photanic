from django.contrib import admin

from . import models

admin.site.register(models.Usuario)
admin.site.register(models.Planta)
admin.site.register(models.Foto)
admin.site.register(models.Comentario)
# Register your models here.
