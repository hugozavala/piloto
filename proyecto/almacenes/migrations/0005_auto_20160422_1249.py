# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0004_auto_20160422_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialpedidoalmacen',
            name='choice_text',
            field=models.CharField(max_length=20, choices=[(b'P/INDM', b'P/INDM'), (b'P/HRM', b'P/HRM'), (b'P/ACC', b'P/ACC'), (b'P/INSTM', b'P/INSTM')]),
        ),
    ]
