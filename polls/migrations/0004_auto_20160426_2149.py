# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-26 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160422_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='question_text1',
            new_name='question_text',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question_text2',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='question_text3',
        ),
    ]