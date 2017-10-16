# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0005_auto_20160422_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacen',
            name='codigo',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
