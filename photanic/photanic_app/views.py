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
from django.contrib.auth.mixins import LoginRequiredMixin


def index (request):
    return render(request, 'photanic_app/index.html')

#Plantas

class Lista_plantas(ListView):
    model = Planta

class Detalles_plantas(DetailView):
    model = Planta

class plantcreateview(LoginRequiredMixin, CreateView):
    model = Planta
    fields = ['common_name','kingdom','phylum','clase','order','family','genus','category']
    success_url = reverse_lazy('index')

class plantUpdateView(LoginRequiredMixin, UpdateView):
    model = Planta
    fields = ['common_name','kingdom','phylum','clase','order','family','genus','category']
    success_url = reverse_lazy('index')

class plantDeleteView(LoginRequiredMixin, DeleteView):
    model = Planta
    success_url='/plant/'

#Fotos
class Lista_fotos(ListView):
    model = Foto

class Detalles_fotos(DetailView):
    model = Foto
    template_name = "./photanic_app/foto_detail.html"

class fotocreateview(LoginRequiredMixin, CreateView):
    model = Foto
    fields = ['Usu','plant','img','place','descrip','time_stamp']
    success_url = reverse_lazy('fotos')

class fotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Foto
    fields = ['Usu','plant','img','place','descrip','time_stamp']
    template_name = "./photanic_app/foto_form.html"
    success_url = reverse_lazy('fotos')

class fotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Foto
    success_url='/foto/'

#Comentario

class Lista_comentarios(ListView):
    model = Comentario

class Detalles_comentarios(DetailView):
    model = Comentario

class comentcreateview(LoginRequiredMixin, CreateView):
    model = Comentario
    fields=['Usu','photo','text','time']
    success_url = reverse_lazy('photos')

class comentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentario
    fields=['Usu','photo','text','time']
    success_url = reverse_lazy('coments')

class comentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    success_url = reverse_lazy('coments')

#Valoraciones

class Lista_valoraciones(ListView):
    model = Valoracion

class Detalles_valoraciones(DetailView):
    model = Valoracion

class ratecreateview(LoginRequiredMixin, CreateView):
    model = Valoracion
    fields=['Usu_valo','art_valo','rate']
    success_url = reverse_lazy('rates')

class rateUpdateView(LoginRequiredMixin, UpdateView):
    model = Valoracion
    fields=['Usu_valo','art_valo','rate']
    success_url = reverse_lazy('rates')

class rateDeleteView(LoginRequiredMixin, DeleteView):
    model = Valoracion
    success_url = reverse_lazy('rates')

#Articulos
class Lista_Articulos(ListView):
    model = Articulo

class Detalles_articulos(DetailView):
    model = Articulo

class articlecreateview(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    success_url = reverse_lazy('articles')

class articleUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    success_url = reverse_lazy('articles')

class articleDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('articles')

#Usuarios
class Lista_usuarios(LoginRequiredMixin, ListView):
    model = User
    template_name = "./photanic_app/user_list.html"

class Detalles_usuarios(LoginRequiredMixin, DetailView):
    model = User

#Registro
class FormUser(CreateView):
    model = User
    form_class = UserForm
    template_name = "./photanic_app/user_form.html"

class Update_User(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEdit
    template_name = "./photanic_app/user_update_form.html"


def aboutus (request):
    return render(request, 'photanic_app/aboutus.html')

def contact(request):
    return render(request, 'photanic_app/contact.html')

def terms(request):
    return render(request, 'photanic_app/terms.html')

