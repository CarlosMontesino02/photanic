# Generated by Django 4.1.2 on 2022-11-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photanic_app', '0002_alter_foto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
