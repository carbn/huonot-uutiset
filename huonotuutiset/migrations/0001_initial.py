# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('title', models.CharField(max_length=128)),
                ('link', models.URLField()),
                ('guid', models.UUIDField(serialize=False, primary_key=True)),
                ('published', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('regex', models.CharField(max_length=256)),
                ('multiplier', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('site_url', models.URLField()),
                ('rss_url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='newsitem',
            name='matches',
            field=models.ManyToManyField(related_name='matches', to='huonotuutiset.Rule'),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='site',
            field=models.ForeignKey(to='huonotuutiset.Site'),
        ),
    ]
