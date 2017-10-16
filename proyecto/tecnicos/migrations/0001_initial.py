# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HorarioDias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=b'codigo', max_length=25)),
                ('numero_horas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='horariodias_horariomes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horariodias', models.ForeignKey(to='tecnicos.HorarioDias')),
            ],
        ),
        migrations.CreateModel(
            name='HorarioHoras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horario', models.CharField(max_length=30, choices=[(b'06:00:00AM a 14:00:00PM', b'06:00:00AM a 14:00:00PM'), (b'14:00:00PM a 22:00:00PM', b'14:00:00PM a 22:00:00PM'), (b'22:00:00PM a 06:00:00AM', b'22:00:00PM a 06:00:00AM')])),
                ('numero_horas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HorarioMes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=b'codigo', max_length=25)),
                ('numero_dias', models.IntegerField()),
                ('horariodias', models.ManyToManyField(to='tecnicos.HorarioDias', through='tecnicos.horariodias_horariomes')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DNI', models.PositiveIntegerField(unique=b'DNI')),
                ('primer_nombre', models.CharField(max_length=30)),
                ('segundo_nombre', models.CharField(max_length=35, null=True, blank=True)),
                ('primer_apellido', models.CharField(max_length=35)),
                ('segundo_apellido', models.CharField(max_length=35, null=True, blank=True)),
                ('edad', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(90)])),
                ('distrito', models.CharField(max_length=30)),
                ('avenida', models.CharField(max_length=30, null=True, blank=True)),
                ('calle', models.CharField(max_length=30, null=True, blank=True)),
                ('urbanizacion', models.CharField(max_length=30, null=True, blank=True)),
                ('manzana', models.CharField(max_length=30, null=True, blank=True)),
                ('jiron', models.CharField(max_length=30, null=True, blank=True)),
                ('lote', models.CharField(max_length=4, null=True, blank=True)),
                ('numero_vivienda', models.IntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(9999)])),
                ('imagen_tecnico', models.ImageField(upload_to=b'imagen_tecnico')),
            ],
        ),
        migrations.AddField(
            model_name='horariohoras',
            name='tecnico',
            field=models.ForeignKey(to='tecnicos.Tecnico'),
        ),
        migrations.AddField(
            model_name='horariodias_horariomes',
            name='horariomes',
            field=models.ForeignKey(to='tecnicos.HorarioMes'),
        ),
        migrations.AddField(
            model_name='horariodias',
            name='horariohoras',
            field=models.ForeignKey(to='tecnicos.HorarioHoras'),
        ),
    ]
