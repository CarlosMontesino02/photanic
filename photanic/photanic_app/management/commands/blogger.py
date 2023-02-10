from django.contrib.auth.models import Group
from gameseek_app.models import User, Client
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth.signals import user_logged_in

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('usuario', type=str, help='Usuario que quieres añadir')


    def handle(self, *args, **kwargs):
        try:
            user_name = kwargs['usuario']
            usuario = Client.objects.get(username=user_name)
            grupo = Group.objects.get(name='Blogger')
            if not grupo in usuario.groups.all():
                usuario.groups.add(grupo)
                print(f" {usuario.username} agregado a {grupo.name} correctamente")

            else:
                print(f"El usuario {usuario.username} ya está en el grupo {grupo.name}" )
        except:
            print(f"Error: {user_name} no existe")
