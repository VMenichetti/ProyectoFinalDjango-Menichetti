# Generated by Django 4.2.4 on 2023-10-07 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0017_alter_pelicula_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='imagen',
            new_name='imagenpelicula',
        ),
    ]
