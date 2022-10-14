from django.shortcuts import render
from photanic_app.models import Usuario, Planta, Foto, Comentario, Articulo, Valoracion
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic.edit import CreateView


def index (request):
    return render(request, 'photanic_app/index.html')

class Lista_plantas(ListView):
    model = Planta

class Detalles_plantas(DetailView):
    model = Planta

class Lista_fotos(ListView):
    model = Foto

class Detalles_fotos(DetailView):
    model = Foto

class Lista_comentarios(ListView):
    model = Comentario

class Detalles_comentarios(DetailView):
    model = Comentario

class Lista_valoraciones(ListView):
    model = Valoracion

class Detalles_valoraciones(DetailView):
    model = Valoracion

class Lista_Articulos(ListView):
    model = Articulo

class Detalles_articulos(DetailView):
    model = Articulo

class Lista_usuarios(ListView):
    model = Usuario

class Detalles_usuarios(DetailView):
    model = Usuario
# Create your views here.
