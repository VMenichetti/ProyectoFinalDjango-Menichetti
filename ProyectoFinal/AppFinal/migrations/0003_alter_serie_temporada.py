# Generated by Django 4.2.4 on 2023-10-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0002_pelicula_serie_delete_peliculas_delete_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='temporada',
            field=models.IntegerField(),
        ),
    ]
