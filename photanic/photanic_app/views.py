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
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

def index (request):
    return render(request, 'photanic_app/index.html')

#Plantas

class search(ListView):
    model = Planta
    template_name="photanic_app/search.html"
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list=Planta.objects.filter(Q(common_name__icontains=query))
        return object_list

class Lista_plantas(ListView):
    model = Planta

class Detalles_plantas(DetailView):
    model = Planta

class plantcreateview(UserPassesTestMixin,LoginRequiredMixin, CreateView):
    model = Planta
    fields = ['common_name','kingdom','phylum','clase','order','family','genus','category']
    success_url = reverse_lazy('index')
    def test_func(self):
        return self.request.user.is_staff

class plantUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Planta
    fields = ['common_name','kingdom','phylum','clase','order','family','genus','category']
    success_url = reverse_lazy('index')
    def test_func(self):
        return self.request.user.is_staff

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
    form_class = FotoForm
    template_name = "./photanic_app/foto_form.html"
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('fotos'))


class fotoUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Foto
    fields = ['plant','img','place','descrip']
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
    form_class = ComentForm
    success_url = reverse_lazy('photos')
    template_name = "./photanic_app/coment_form.html"
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('coments'))

class comentUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Comentario
    fields=['user','photo','text','time']
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
#Articulos
class Lista_Articulos(ListView):
    model = Articulo

class Detalles_articulos(DetailView):
    model = Articulo
    def get_object(self):
        obj = super().get_object()
        todos_ratings= obj.valoracion_set.all()
        if len( todos_ratings) != 0:
            cuenta=0
            for punto in  todos_ratings:
                cuenta+=int(punto.rate)
            if not obj.rating == int(cuenta)/len( todos_ratings): #Calculo de la valoración
                obj.rating = int(cuenta)/len(todos_ratings)
                obj.save()
                obj=Articulo.objects.get(title=obj) #Autoguardamos con el título del articulo
        objeto_final=obj
        return objeto_final
    def get_context_data(self, **kwargs):
        context = super(Detalles_articulos, self).get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            list = Valoracion.objects.filter(user=self.request.user, art_valo=super().get_object())
            if len(list) == 0:
                context['already'] = False
            else:   
                context['already'] = True
        return context

class articlecreateview(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    success_url = reverse_lazy('articles')
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('articles'))

class articleUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    success_url = reverse_lazy('articles')
    def test_func(self):
        try:

            return User.objects.get(username=self.request.user.username)==Articulo.objects.get(user=Articulo.user.get("username"))
        except:
            return False

class articleDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('articles')
    def test_func(self):
        try:
            return User.objects.get(username=self.request.user.username)==Articulo.objects.get(user_art=self.kwargs.get("user_art"))
        except:
            return False    


#Valoraciones

class Lista_valoraciones(ListView):
    model = Valoracion

class Detalles_valoraciones(DetailView):
    model = Valoracion

class ratecreateview(LoginRequiredMixin,CreateView):
    login_url = 'user-add'
    model = Valoracion
    fields = ['rate']
    def form_valid(self, form):
        url=self.request.get_full_path()
        urlcad=url.split("/")
        objeto=Articulo.objects.get(pk=int(urlcad[3]))
        form.instance.art_valo = objeto
        form.instance.user = self.request.user
        list = Valoracion.objects.filter(user=self.request.user, art_valo=objeto)
        if len(list) == 0:
            form.save()
            return redirect('articles_details', pk=urlcad[3])
        else:
            raise PermissionDenied
    def get_context_data(self, **kwargs):
        url=self.request.get_full_path()
        urlcad=url.split("/")
        objeto=Articulo.objects.get(pk=int(urlcad[3]))
        context = super(ratecreateview, self).get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            list = Valoracion.objects.filter(user=self.request.user, art_valo=objeto)
            if len(list) == 0:  
                context['already'] = False
            else:   
                context['already'] = True
        return context

class rateUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Valoracion
    fields=['user_valo','art_valo','rate']
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

#Usuarios
class Lista_usuarios(LoginRequiredMixin, ListView):
    model = User
    template_name = "./photanic_app/user_list.html"

class Detalles_usuarios(LoginRequiredMixin, DetailView):
    model = User

    def get_context_data(self, **kwargs):
        queryset = User.objects.all()
        context_object_name = 'user'
        context = super().get_context_data(**kwargs)
        context['articulos']=Articulo.objects.filter(user=self.kwargs.get("pk"))
        return context
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
