# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('huonotuutiset', '0004_newsitem_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='site',
            field=models.ForeignKey(related_name='newsitems', to='huonotuutiset.Site'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
