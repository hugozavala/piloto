# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rotulo', models.CharField(unique=b'rotulo', max_length=10)),
                ('nombre', models.CharField(max_length=40)),
                ('tipo_equipo', models.CharField(max_length=10, choices=[(b'AA', b'AA'), (b'EE', b'EE'), (b'V', b'V')])),
                ('marca', models.CharField(max_length=20, null=True, blank=True)),
                ('modelo', models.CharField(max_length=20, null=True, blank=True)),
                ('numero_serie', models.CharField(max_length=30, null=True, blank=True)),
                ('imagen_equipo', models.ImageField(upload_to=b'imagen_equipo')),
                ('mantenimientos_realizados', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Estacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=b'codigo', max_length=15)),
                ('nombre', models.CharField(max_length=40)),
                ('caracteristicas', models.TextField(max_length=200, null=True, blank=True)),
                ('equipo', models.ForeignKey(to='equipos.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialEquipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_mantenimiento', models.CharField(max_length=200)),
                ('question', models.ForeignKey(to='equipos.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Parte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=b'nombre', max_length=30)),
                ('caracteristicas', models.TextField(max_length=850, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=b'codigo', max_length=20)),
                ('datos', models.TextField(max_length=400, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='parte',
            name='pieza',
            field=models.ForeignKey(to='equipos.Pieza'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='partes',
            field=models.ForeignKey(to='equipos.Parte'),
        ),
    ]
