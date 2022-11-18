from django.shortcuts import render
from photanic_app.models import *
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import *


def index (request):
    return render(request, 'photanic_app/index.html')

#Plantas

class Lista_plantas(ListView):
    model = Planta

class Detalles_plantas(DetailView):
    model = Planta

class plantcreateview(CreateView):
    model = Planta
    fields = ['common_name','kingdom','phylum','clase','order','family','genus','category']
    success_url = reverse_lazy('index')

class plantUpdateView(UpdateView):
    model = Planta
    fields = ['common_name','kingdom','phylum','clase','order','family','genus','category']
    success_url = reverse_lazy('index')

class plantDeleteView(DeleteView):
    model = Planta
    success_url='/plant/'

#Fotos
class Lista_fotos(ListView):
    model = Foto

class Detalles_fotos(DetailView):
    model = Foto
    template_name = "./photanic_app/foto_detail.html"

class fotocreateview(CreateView):
    model = Foto
    fields = ['Usu','plant','img','place','descrip','time_stamp']
    success_url = reverse_lazy('fotos')

class fotoUpdateView(UpdateView):
    model = Foto
    fields = ['Usu','plant','img','place','descrip','time_stamp']
    template_name = "./photanic_app/foto_form.html"
    success_url = reverse_lazy('fotos')

class fotoDeleteView(DeleteView):
    model = Foto
    success_url='/foto/'

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
    form_class = ArticuloForm
    success_url = reverse_lazy('articles')

class articleUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    success_url = reverse_lazy('articles')

class articleDeleteView(DeleteView):
    model = Articulo
    success_url = reverse_lazy('articles')

#Usuarios
class Lista_usuarios(ListView):
    model = User
    template_name = "./photanic_app/user_list.html"

class Detalles_usuarios(DetailView):
    model = User

#Registro
class FormUser(CreateView):
    model = User
    form_class = UserForm
    template_name = "./photanic_app/user_form.html"

class Update_User(UpdateView):
    model = User
    form_class = UserEdit
    template_name = "./photanic_app/user_update_form.html"


def aboutus (request):
    return render(request, 'photanic_app/aboutus.html')

def contact(request):
    return render(request, 'photanic_app/contact.html')

