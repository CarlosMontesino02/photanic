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

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planta
        fields = ['common_name','kingdom','phylum','clase','order','family','genus','category']

# ViewSets define the view behavior.
class PlantViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'plantas', PlantViewSet)