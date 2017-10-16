# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tecnicos', '0002_auto_20160422_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horariomes',
            name='codigo',
            field=models.CharField(unique=b'codigo', max_length=30, choices=[(b'ENERO 2016', b'ENERO 2016'), (b'FEBRERO 2016', b'FEBRERO 2016'), (b'MARZO 2016', b'MARZO 2016'), (b'ABRIL 2016', b'ABRIL 2016'), (b'MAYO 2016', b'MAYO 2016'), (b'JUNIO 2016', b'JUNIO 2016'), (b'JULIO 2016', b'JULIO 2016'), (b'AGOSTO 2016', b'AGOSTO 2016'), (b'SEPTIEMBRE 2016', b'SEPTIEMBRE 2016'), (b'OCTUBRE 2016', b'OCTUBRE 2016'), (b'NOVIEMBRE 2016', b'NOVIEMBRE 2016'), (b'DICIEMBRE 2016', b'DICIEMBRE 2016')]),
        ),
    ]
