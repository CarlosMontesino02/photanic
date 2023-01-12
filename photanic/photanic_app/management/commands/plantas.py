from photanic_app.models import Planta
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', type=int)

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            Planta.objects.create(common_name=get_random_string(8),kingdom=get_random_string(8),phylum=get_random_string(8),clase=get_random_string(8),order=get_random_string(8),family=get_random_string(8),genus=get_random_string(8),category=get_random_string(8),)