from pyexpat import model
from statistics import mode
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django_countries.fields import CountryField

class User(AbstractUser):
    country = CountryField()
    new = 'NW'
    amateur = 'AM'
    profesional = 'PR'
    master = 'MS'

    RANKS = [
        (new, 'New'),
        (amateur, 'Amateur'),
        (profesional, 'Profesional'),
        (master, 'Master'),
    ]
    rank = models.CharField(
    'Rango*',
    max_length=2,
    choices=RANKS,
    default=new,
    null=True
    )
    birth_date = models.DateTimeField('Fecha de nacimiento*',auto_now=False,)
    
    def get_absolute_url(self):
        return reverse('usuarios-detalles', kwargs={'pk': self.pk})

class Planta(models.Model):
    common_name = models.CharField(max_length=23)
    kingdom = models.CharField(max_length=23)
    phylum = models.CharField(max_length=23)
    clase = models.CharField(max_length=23)
    order = models.CharField(max_length=23)
    family = models.CharField(max_length=23)
    genus = models.CharField(max_length=23)
    category = models.CharField(max_length=23)
    def __str__(self):
        return self.common_name

class Foto(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plant = models.ForeignKey(Planta, on_delete=models.CASCADE)
    img = models.ImageField(upload_to ='img/')
    place = models.CharField(max_length=23)
    descrip = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now=True)

class Comentario(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ForeignKey(Foto, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)

class Articulo(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plant_art = models.ForeignKey(Planta, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Valoracion(models.Model):
    user_valo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    art_valo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    rate = models.IntegerField()
    # Create your models here.
