# Generated by Django 4.2.7 on 2023-12-18 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lugares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.AlterField(
            model_name='post',
            name='cuerpo',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Proyecto/assets/'),
        ),
    ]
