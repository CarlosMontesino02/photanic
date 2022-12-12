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
from django.contrib.auth.mixins import UserPassesTestMixin


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

class plantUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Planta
    fields = ['common_name','kingdom','phylum','clase','order','family','genus','category']
    success_url = reverse_lazy('index')
    def test_func(self):
        try:
            return Planta.objects.get(pk=self.request.user.pk)==Planta.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class plantDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Planta
    success_url='/plant/'
    def test_func(self):
        try:
            return Planta.objects.get(pk=self.request.user.pk)==Planta.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

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

class fotoUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Foto
    fields = ['Usu','plant','img','place','descrip','time_stamp']
    template_name = "./photanic_app/foto_form.html"
    success_url = reverse_lazy('fotos')
    def test_func(self):
        try:
            return Foto.objects.get(pk=self.request.user.pk)==Foto.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class fotoDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Foto
    success_url='/foto/'
    def test_func(self):
        try:
            return Foto.objects.get(pk=self.request.user.pk)==Foto.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
#Comentario

class Lista_comentarios(ListView):
    model = Comentario

class Detalles_comentarios(DetailView):
    model = Comentario

class comentcreateview(LoginRequiredMixin, CreateView):
    model = Comentario
    fields=['Usu','photo','text','time']
    success_url = reverse_lazy('photos')

class comentUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Comentario
    fields=['Usu','photo','text','time']
    success_url = reverse_lazy('coments')
    def test_func(self):
        try:
            return Comentario.objects.get(pk=self.request.user.pk)==Comentario.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class comentDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Comentario
    success_url = reverse_lazy('coments')
    def test_func(self):
        try:
            return Comentario.objects.get(pk=self.request.user.pk)==Comentario.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
#Valoraciones

class Lista_valoraciones(ListView):
    model = Valoracion

class Detalles_valoraciones(DetailView):
    model = Valoracion

class ratecreateview(LoginRequiredMixin, CreateView):
    model = Valoracion
    fields=['Usu_valo','art_valo','rate']
    success_url = reverse_lazy('rates')
    success_url = reverse_lazy('articles')

class rateUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Valoracion
    fields=['Usu_valo','art_valo','rate']
    success_url = reverse_lazy('rates')
    def test_func(self):
        try:
            return Valoracion.objects.get(pk=self.request.user.pk)==Valoracion.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class rateDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Valoracion
    success_url = reverse_lazy('rates')
    def test_func(self):
        try:
            return Valoracion.objects.get(pk=self.request.user.pk)==Valoracion.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

#Articulos
class Lista_Articulos(ListView):
    model = Articulo

class Detalles_articulos(DetailView):
    model = Articulo

class articlecreateview(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    success_url = reverse_lazy('articles')
    success_url = reverse_lazy('articles')

class articleUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    success_url = reverse_lazy('articles')
    def test_func(self):
        try:
            return User.objects.get(username=self.request.user.username)==Articulo.objects.get(Usu_art=self.kwargs.get("Usu_art"))
        except:
            return False

class articleDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('articles')
    def test_func(self):
        try:
            return User.objects.get(username=self.request.user.username)==Articulo.objects.get(Usu_art=self.kwargs.get("Usu_art"))
        except:
            return False

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

class Update_User(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEdit
    template_name = "./photanic_app/user_update_form.html"
    def test_func(self):
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False


def aboutus (request):
    return render(request, 'photanic_app/aboutus.html')

def contact(request):
    return render(request, 'photanic_app/contact.html')

def terms(request):
    return render(request, 'photanic_app/terms.html')