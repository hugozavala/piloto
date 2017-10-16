# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0003_auto_20160420_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialpedidoalmacen',
            name='choice_text',
            field=models.CharField(max_length=20, choices=[(b'P/INDM', b'P/INDM'), (b'P/HRM', b'P/HRM'), (b'P/ACC', b'P/ACC'), (b'P/HRM', b'P/HRM')]),
        ),
    ]
