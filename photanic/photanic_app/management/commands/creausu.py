from photanic_app.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', type=int)
    
    def handle(self, *args, **kwargs):
        usernames = ['abusivesimplistic','aircraft quadriceps',
'anyway-guillemot','booger$scruined','earnest-bollard','eyeglasses*abundant',
'gravelly.unripe','sandalunderstood!','highjumptogether','suffix_pallograph',
'prettying^dismiss','limitation_dromond','miserable_wussle','purring.rostary',
'scaffoldinglukewarm','sledding congress','turtlegrapping','walloverpottery',
'wrestlers_scrawny']
        cont=1
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=usernames[cont], email='ben@ben.com', password='Contraseña1234')
            cont+=1