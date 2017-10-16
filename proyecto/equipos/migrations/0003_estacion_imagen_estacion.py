# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0002_auto_20160420_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacion',
            name='imagen_estacion',
            field=models.ImageField(default=int, upload_to=b'imagen_estacion'),
            preserve_default=False,
        ),
    ]
