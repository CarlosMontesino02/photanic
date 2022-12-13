from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from .api import *

urlpatterns = [
    #index
    path('', index, name='index'),
    
    #plantas
    path('plant/', Lista_plantas.as_view(), name="plants"),
    path('plant/<int:pk>/', Detalles_plantas.as_view(), name='plants_details'),
    path('plant/add/', plantcreateview.as_view(), name="plant-add"),
    path('plant/<int:pk>/update', plantUpdateView.as_view(), name='plant-update'),
    path('plant/<int:pk>/delete/', plantDeleteView.as_view(), name='plant-delete'),
    path('plant/search', search.as_view(), name="search"),
   
    #Fotos
    path('foto/',Lista_fotos.as_view(), name="fotos"),
    path('foto/<int:pk>/', Detalles_fotos.as_view(), name='foto_details'),
    path('foto/add/', fotocreateview.as_view(), name="foto-add"),
    path('foto/<int:pk>/update/', fotoUpdateView.as_view(), name='foto-update'),
    path('foto/<int:pk>/delete/', fotoDeleteView.as_view(), name='foto-delete'),
   
    #Articulos
    path('articles/', Lista_Articulos.as_view(), name="articles"),
    path('articles/<int:pk>/', Detalles_articulos.as_view(), name="articles_details"),
    path('articles/add/', articlecreateview.as_view(), name="article-add"),
    path('articles/<int:pk>/update/', articleUpdateView.as_view(), name='article-update'),
    path('articles/<int:pk>/delete/', articleDeleteView.as_view(), name='article-delete'),
  
    #Comentarios
    path('coments', Lista_comentarios.as_view(), name="coments"),
    path('coments/<int:pk>/', Detalles_comentarios.as_view(), name="coments_details"),
    path('coment/add/', comentcreateview.as_view(), name="coment-add"),
    path('coment/<int:pk>/update/', comentUpdateView.as_view(), name='coment-update'),
    path('coment/<int:pk>/delete/', comentDeleteView.as_view(), name='coment-delete'),

    #Valoraciones
    path('rate', Lista_comentarios.as_view(), name="rates"),
    path('rate/<int:pk>/', Detalles_valoraciones.as_view(), name="rates_details"),
    path('rate/add/', ratecreateview.as_view(), name="rate-add"),
    path('rate/<int:pk>/update/', rateUpdateView.as_view(), name='rate-update'),
    path('rate/<int:pk>/delete/', rateDeleteView.as_view(), name='rate-delete'),

    #Usuario
    path('usuarios/', Lista_usuarios.as_view(), name="usuarios-lista"),
    path('usuarios/<int:pk>', Detalles_usuarios.as_view(), name="usuarios-detalles"),
    path('usuarios/<int:pk>/update', Update_User.as_view(), name="usuarios-update"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)