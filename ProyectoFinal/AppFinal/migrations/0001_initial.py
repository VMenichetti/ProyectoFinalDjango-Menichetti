# Generated by Django 4.2.5 on 2023-10-01 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=40)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('reseña', models.CharField(max_length=150)),
                ('youtube', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=40)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('temporada', models.TextField()),
                ('descripcion', models.CharField(max_length=150)),
                ('reseña', models.CharField(max_length=150)),
                ('youtube', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('enlace_web', models.URLField(blank=True)),
                ('imagen', models.ImageField(blank=True, upload_to='#')),
            ],
        ),
    ]
