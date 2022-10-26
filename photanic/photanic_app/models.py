from pyexpat import model
from statistics import mode
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
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
    max_length=2,
    choices=RANKS,
    default=amateur,
    )
    birth_date = models.DateTimeField(auto_now=False, auto_now_add=False)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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
    Usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    plant = models.ForeignKey(Planta, on_delete=models.CASCADE)
    img = models.ImageField()
    place = models.CharField(max_length=23)
    descrip = models.CharField(max_length=200)
    time_stamp = models.DateTimeField()

class Comentario(models.Model):
    Usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    photo = models.ForeignKey(Foto, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    time = models.DateTimeField()

class Articulo(models.Model):
    title = models.CharField(max_length=23)
    text = models.CharField(max_length=1500)
    Usu_art = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    plant_art = models.ForeignKey(Planta, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Valoracion(models.Model):
    Usu_valo = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    art_valo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    rate = models.IntegerField()
    # Create your models here.