from django.contrib.auth.models import Group
from photanic_app.models import User
from django.contrib.auth.signals import (user_logged_in,
                                        user_logged_out,
                                        user_login_failed)
from django.dispatch import receiver
from django.core.mail import BadHeaderError,send_mail

@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    try:
        grupo = Group.objects.get(name='Bloggers')
        usuario = User.objects.get(username=user)
        c = User.objects.get(username=user).email
    except:
         print(f"ERROR: No se ha podido asignar alguna/s de las variables.")

    if not grupo in usuario.groups.all():
        usuario.groups.add(grupo.id)
        usuario.save()
        print(f"El usuario, {usuario.username}, se ha añadido al grupo, {grupo.name}, correctamente.")
        send_mail(
            'Hola!, te hemos asignado al grupo Bloggers',
            'Apartir de ahora tienes la capacidad de escribir artículos en nuestra aplicación!',
            'photanic.oficial@gmail.com',
            [c],
            fail_silently=False,
        )
    else:
        print(f"ERROR: El usuario, {usuario.username}, ya se encuentra al grupo {grupo.name}.")
