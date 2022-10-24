from django.shortcuts import render
from photanic_app.models import *
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


def index (request):
    return render(request, 'photanic_app/index.html')

#Plantas

class Lista_plantas(ListView):
    model = Planta

class Detalles_plantas(DetailView):
    model = Planta

class plantcreateview(CreateView):
    model = Planta
    fields = ['id','kingdom','phylum','clase','order','family','genus','category']
    success_url = reverse_lazy('')

class plantUpdateView(UpdateView):
    model = Planta
    fields = ['id','kingdom','phylum','clase','order','family','genus','category']

class plantDeleteView(DeleteView):
    model = Planta
    success_url = reverse_lazy('plants')

#Fotos
class Lista_fotos(ListView):
    model = Foto

class Detalles_fotos(DetailView):
    model = Foto

class fotocreateview(CreateView):
    model = Foto
    fields = ['Usu','plant','img','place','descrip','time_stamp']
    success_url = reverse_lazy('')

class fotoUpdateView(UpdateView):
    model = Foto
    fields = ['Usu','plant','img','place','descrip','time_stamp']

class fotoDeleteView(DeleteView):
    model = Foto
    success_url = reverse_lazy('fotos')
#Comentario

class Lista_comentarios(ListView):
    model = Comentario

class Detalles_comentarios(DetailView):
    model = Comentario

class comentcreateview(CreateView):
    model = Comentario
    fields=['Usu','photo','text','time']
    success_url = reverse_lazy('photos')

class comentUpdateView(UpdateView):
    model = Comentario
    fields=['Usu','photo','text','time']
    success_url = reverse_lazy('coments')

class comentDeleteView(DeleteView):
    model = Comentario
    success_url = reverse_lazy('coments')

#Valoraciones

class Lista_valoraciones(ListView):
    model = Valoracion

class Detalles_valoraciones(DetailView):
    model = Valoracion

class ratecreateview(CreateView):
    model = Valoracion
    fields=['Usu_valo','art_valo','rate']
    success_url = reverse_lazy('rates')

class rateUpdateView(UpdateView):
    model = Valoracion
    fields=['Usu_valo','art_valo','rate']
    success_url = reverse_lazy('rates')

class rateDeleteView(DeleteView):
    model = Valoracion
    success_url = reverse_lazy('rates')

#Articulos
class Lista_Articulos(ListView):
    model = Articulo

class Detalles_articulos(DetailView):
    model = Articulo

class articlecreateview(CreateView):
    model = Articulo
    fields=['title','text','Usu_art','plant_art']
    success_url = reverse_lazy('articles')

class articleUpdateView(UpdateView):
    model = Articulo
    fields=['title','text','Usu_art','plant_art']
    success_url = reverse_lazy('articles')

class articleDeleteView(DeleteView):
    model = Articulo
    success_url = reverse_lazy('articles')

#Usuarios
class Lista_usuarios(ListView):
    model = Usuario

class Detalles_usuarios(DetailView):
    model = Usuario

# Create your views here.
