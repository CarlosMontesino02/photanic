"""photanic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from photanic_app.views import index, Lista_plantas, Lista_fotos, Lista_comentarios, Lista_valoraciones, Lista_Articulos, Lista_usuarios
from photanic_app.views import Detalles_plantas, Detalles_fotos, Detalles_comentarios, Detalles_valoraciones, Detalles_articulos, Detalles_usuarios
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('plants/', Lista_plantas.as_view(), name="plants"),
    path('', index, name='index'),
    path('photos/',Lista_fotos.as_view(), name="fotos"),
    path('articles/', Lista_Articulos.as_view(), name="articles"),
    path('profiles/', Lista_usuarios.as_view(), name="profiles"),
    path('plants/<int:pk>/', Detalles_plantas.as_view(), name='plants_details'),
    path('articles/<int:pk>/', Detalles_articulos.as_view(), name="articles_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
