# Generated by Django 4.2.7 on 2023-12-19 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0002_lugares_restaurantes_delete_cliente_delete_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Proyecto/media/'),
        ),
    ]
