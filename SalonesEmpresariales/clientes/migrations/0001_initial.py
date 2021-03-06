# Generated by Django 4.0.3 on 2022-04-11 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='documento de identidad')),
                ('nombre', models.CharField(max_length=32, verbose_name='nombre del cliente')),
                ('apellido', models.CharField(max_length=32, verbose_name='apellido del cliente')),
                ('telefono', models.IntegerField(max_length=10, verbose_name='telefono del cliente')),
                ('correo', models.EmailField(max_length=120, verbose_name='correo del cliente')),
                ('departamento', models.CharField(max_length=32, verbose_name='departamento del cliente')),
                ('ciudad', models.CharField(max_length=32, verbose_name='ciudad del cliente')),
                ('edad', models.IntegerField(max_length=3, verbose_name='edad del cliente')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creado en')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='actualizado en')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creado en')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='actualizado en')),
                ('fecha_evento', models.DateTimeField(verbose_name='Fecha de evento')),
                ('cantidad_personas', models.IntegerField(max_length=3, verbose_name='Cantidad de Personas en el evento')),
                ('motivo', models.CharField(max_length=32, verbose_name='Motivo del evento')),
                ('observaciones', models.CharField(max_length=32, verbose_name='Observaciones del evento')),
                ('Estado', models.CharField(max_length=32, verbose_name='Estado del evento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'evento',
                'verbose_name_plural': 'eventos',
            },
        ),
    ]
