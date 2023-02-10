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
        c = User.objects.get(username=user).mail
        if not group in usu.groups.all():
                usu.groups.add(group)
                usu.save()
                subject = 'Añadido al grupo Bloggers'
                mensaje = 'Este mail te informa de que tienes acceso a las caracterśiitcsa del grupo Bloggers'
                from_email = 'qhgx.ghfaa89@nefyp.com'
                send_mail(subject,mensaje,from_email, [f'{c}'])
    except:
        print(f"Hubo un error durante la agregación del usuario")