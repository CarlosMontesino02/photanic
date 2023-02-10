from django.contrib.auth.models import Group
from photanic_app.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    try:
        group = Group.objects.get(name='Blogger')
        usu = User.objects.get(username=user)
        if not group in usu.groups.all():
                usu.groups.add(group)
                usu.save()
    except:
        print(f"Hubo un error durante la agregación del usuario")