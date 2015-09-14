# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('huonotuutiset', '0002_auto_20150914_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='link',
            field=models.URLField(max_length=512),
        ),
    ]
