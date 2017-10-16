# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0002_remove_almacen_equipos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacen',
            name='codigo',
            field=models.CharField(max_length=30),
        ),
    ]
