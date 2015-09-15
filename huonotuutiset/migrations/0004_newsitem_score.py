# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('huonotuutiset', '0003_auto_20150914_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]
