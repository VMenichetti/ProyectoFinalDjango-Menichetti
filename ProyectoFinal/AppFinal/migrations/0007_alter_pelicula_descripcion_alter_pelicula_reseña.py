# Generated by Django 4.2.4 on 2023-10-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0006_alter_pelicula_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='descripcion',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='reseña',
            field=models.CharField(max_length=600),
        ),
    ]
