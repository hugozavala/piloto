# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=b'codigo', max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30, null=True, blank=True)),
                ('modelo', models.CharField(max_length=25, null=True, blank=True)),
                ('fecha_vencimiento', models.DateField(null=True, blank=True)),
                ('imagen_accesorio', models.ImageField(null=True, upload_to=b'imagen_accesorio', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=30)),
                ('nombre', models.CharField(max_length=45)),
                ('equipos', models.ForeignKey(to='equipos.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=b'codigo', max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30, null=True, blank=True)),
                ('imagen_herramienta', models.ImageField(upload_to=b'imagen_herramienta')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialPedidoAlmacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=20, choices=[(b'P/INDM', b'P/INDM'), (b'P/HRM', b'P/HRM'), (b'P/ACC', b'P/ACC')])),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Indumentaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=b'codigo', max_length=15)),
                ('nombre', models.CharField(max_length=30)),
                ('talla', models.CharField(max_length=30)),
                ('imagen_indumentaria', models.ImageField(upload_to=b'imagen_indumentaria')),
            ],
        ),
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=b'codigo', max_length=15)),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=30, null=True, blank=True)),
                ('imagen_instrumento', models.ImageField(upload_to=b'imagen_instrumento')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoAlmacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=30)),
                ('nombre', models.CharField(max_length=45)),
                ('fecha_pedido', models.DateTimeField()),
                ('accesorio', models.ForeignKey(to='almacenes.Accesorio')),
                ('herramienta', models.ForeignKey(to='almacenes.Herramienta')),
                ('indumentaria', models.ForeignKey(to='almacenes.Indumentaria')),
                ('instrumento', models.ForeignKey(to='almacenes.Instrumento')),
            ],
        ),
        migrations.AddField(
            model_name='historialpedidoalmacen',
            name='pedido_almacen',
            field=models.ForeignKey(to='almacenes.PedidoAlmacen'),
        ),
        migrations.AddField(
            model_name='almacen',
            name='pedido_almacen',
            field=models.ForeignKey(to='almacenes.PedidoAlmacen'),
        ),
    ]
