from photanic_app.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', type=int)
    
    def handle(self, *args, **kwargs):
        usernames = ['Mastermind434','LeBronYames',
'Yuri Tarded','MrPoPo','Julian','Joe Mama',
'Ligma','sandalunderstood!','highjumptogether','suffix_pallograph',
'prettying^dismiss','limitation_dromond','miserable_wussle','purring.rostary',
'scaffoldinglukewarm','sledding congress','turtlegrapping','walloverpottery',
'wrestlers_scrawny']
        cont=0
        total = kwargs['total']
        for i in range(total):
            mail=get_random_string(5)
            dominio=get_random_string(5)
            email= mail+"@"+dominio+".com"
            User.objects.create_user(username=usernames[cont], email=email, password='Contraseña1234')
            cont+=1
