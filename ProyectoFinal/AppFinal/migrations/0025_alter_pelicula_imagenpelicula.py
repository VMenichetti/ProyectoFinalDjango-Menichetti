# Generated by Django 4.2.4 on 2023-10-08 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0024_alter_pelicula_imagenpelicula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagenpelicula',
            field=models.ImageField(blank=True, null=True, upload_to='pelicula'),
        ),
    ]
