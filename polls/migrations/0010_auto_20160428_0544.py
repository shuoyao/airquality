# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-28 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20160428_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='income',
            field=models.CharField(choices=[(b'$25,000 or less', b'$25,000 or less'), (b'$25,001 - $50,000', b'$25,001 - $50,000'), (b'$50,001 - $75,000', b'$50,001 - $75,000'), (b'$75,001 - $100,000', b'$75,001 - $100,000'), (b'Above $100,000', b'Above $100,000')], default=1, max_length=200),
        ),
    ]
