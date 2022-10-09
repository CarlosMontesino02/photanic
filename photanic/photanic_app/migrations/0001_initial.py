# Generated by Django 4.1.1 on 2022-10-09 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('common_name', models.CharField(max_length=23, primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('kingdom', models.CharField(max_length=23)),
                ('phylum', models.CharField(max_length=23)),
                ('clase', models.CharField(max_length=23)),
                ('order', models.CharField(max_length=23)),
                ('family', models.CharField(max_length=23)),
                ('genus', models.CharField(max_length=23)),
                ('category', models.CharField(max_length=23)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nomUsu', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=20)),
                ('rank', models.CharField(choices=[('NW', 'New'), ('AM', 'Amateur'), ('PR', 'Profesional'), ('MS', 'Master')], default='AM', max_length=2)),
                ('birth_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='')),
                ('place', models.CharField(max_length=23)),
                ('descrip', models.CharField(max_length=200)),
                ('time_stamp', models.DateTimeField()),
                ('Usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photanic_app.usuario')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photanic_app.planta')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('Usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photanic_app.usuario')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photanic_app.foto')),
            ],
        ),
    ]
