from pyexpat import model
from statistics import mode
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
class Usuario(models.Model):
    nomUsu = models.CharField(max_length=18, primary_key=True)
    mail = models.EmailField(max_length=254)
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

class Planta(models.Model):
    common_name = models.CharField(max_length=23, primary_key=True)
    id = models.IntegerField()
    kingdom = models.CharField(max_length=23)
    phylum = models.CharField(max_length=23)
    clase = models.CharField(max_length=23)
    order = models.CharField(max_length=23)
    family = models.CharField(max_length=23)
    genus = models.CharField(max_length=23)
    category = models.CharField(max_length=23)

class Foto(models.Model):
    id = models.IntegerField(primary_key=True)
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
    id_art = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=23)
    text = models.CharField(max_length=1500)
    Usu_art = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    plant_art = models.ForeignKey(Planta, on_delete=models.CASCADE)

class Valoracion(models.Model):
    Usu_valo = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    art_valo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    rate = models.IntegerField()
    # Create your models here.
