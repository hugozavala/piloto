# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parte',
            name='imagen_parte',
            field=models.ImageField(default=int, upload_to=b'imagen_parte'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pieza',
            name='imagen_pieza',
            field=models.ImageField(default=int, upload_to=b'imagen_pieza'),
            preserve_default=False,
        ),
    ]
