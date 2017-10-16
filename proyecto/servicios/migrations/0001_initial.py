# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tecnicos', '0003_auto_20160422_1122'),
        ('equipos', '0003_estacion_imagen_estacion'),
        ('almacenes', '0003_auto_20160420_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cronograma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=b'codigo', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialConformidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=20, choices=[(b'Si', b'Si'), (b'Puede mejorar', b'Puede mejorar'), (b'No', b'No')])),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=b'codigo', max_length=30)),
                ('tareas', models.TextField(max_length=250)),
                ('tipo_mantenimiento', models.CharField(max_length=30, choices=[(b'Preventivo', b'Preventivo'), (b'Correctivo', b'Correctivo'), (b'Generales', b'Generales')])),
                ('imagen_inicial', models.ImageField(upload_to=b'imagen_servicio/imagen_inicial')),
                ('imagen_final', models.ImageField(upload_to=b'imagen_servicio/imagen_final')),
                ('question_text', models.CharField(max_length=200)),
                ('equipo', models.ForeignKey(to='equipos.Equipo')),
                ('pedido_almacen', models.ForeignKey(to='almacenes.PedidoAlmacen')),
                ('tecnico', models.ForeignKey(to='tecnicos.Tecnico')),
            ],
        ),
        migrations.CreateModel(
            name='servicio_cronograma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_termino', models.DateTimeField()),
                ('cronograma', models.ForeignKey(to='servicios.Cronograma')),
                ('servicio', models.ForeignKey(to='servicios.Servicio')),
            ],
        ),
        migrations.AddField(
            model_name='historialconformidad',
            name='servicio',
            field=models.ForeignKey(to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='cronograma',
            name='servicio',
            field=models.ManyToManyField(to='servicios.Servicio', through='servicios.servicio_cronograma'),
        ),
    ]
