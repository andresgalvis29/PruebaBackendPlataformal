# Generated by Django 4.0.3 on 2022-04-11 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_evento_fecha_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='Estado',
            field=models.CharField(choices=[('confirmado', 'Evento Confirmado'), ('no confirmado', 'Evento no confirmado')], max_length=32, verbose_name='Estado del evento'),
        ),
    ]
