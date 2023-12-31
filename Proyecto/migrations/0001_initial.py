# Generated by Django 4.2.7 on 2023-12-18 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('titulo', models.CharField(max_length=30)),
                ('subtitulo', models.CharField(max_length=30)),
                ('cuerpo', models.CharField(max_length=250)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='producto_imagen/')),
                ('lugar', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(max_length=30)),
            ],
        ),
    ]
