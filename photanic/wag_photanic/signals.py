from django.contrib.auth.models import Group
from photanic_app.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    try:
        group = Group.objects.get(name='Blogger')
        usu = User.objects.get(username=user)
        c = User.objects.get(username=user).email
        if not group in usu.groups.all():
                usu.groups.add(group)
                usu.save()
                send_mail(
                'Hola!, te hemos asignado al grupo Bloggers',
                'Apartir de ahora tienes la capacidad de escribir artículos en nuestra aplicación!',
                'photanic.oficial@gmail.com',
                [c],
                fail_silently=False,
            )
    except:
        print(f"Hubo un error durante la agregación del usuario")