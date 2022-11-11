from django.urls import path, include
from .models import *
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff','country','birth_date','rank']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Planta
class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planta
        fields = ['common_name','kingdom','phylum','clase','order','family','genus','category']

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantSerializer

#Foto
class FotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foto
        fields = ['Usu','plant','img','place','descrip','time_stamp']

class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer

class ArticuloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articulo
        fields = ['title', 'text', 'Usu_art', 'plant_art']

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'plantas', PlantViewSet)
router.register(r'fotos', FotoViewSet)
router.register(r'articulos', ArticuloViewSet)
