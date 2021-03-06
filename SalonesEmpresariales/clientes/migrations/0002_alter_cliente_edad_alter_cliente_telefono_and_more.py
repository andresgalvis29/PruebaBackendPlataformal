# Generated by Django 4.0.3 on 2022-04-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(verbose_name='edad del cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=11, verbose_name='telefono del cliente'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='cantidad_personas',
            field=models.IntegerField(verbose_name='Cantidad de Personas en el evento'),
        ),
    ]
