from django.urls import path, include
from .models import *
from rest_framework import routers, serializers, viewsets

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff','country','birth_date','rank']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

# ViewSets define the view behavior.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Planta
class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planta
        fields = ['common_name','kingdom','phylum','clase','order','family','genus','category']
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]

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

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ArticuloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articulo
        fields = ['title', 'text', 'Usu_art', 'plant_art']
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'plantas', PlantViewSet)
router.register(r'fotos', FotoViewSet)
router.register(r'articulos', ArticuloViewSet)
#router.register(r'comentarios', ComentarioViewSet)
#router.register(r'valoraciones', ValoracionViewSet)