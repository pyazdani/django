# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='added too late'),
            preserve_default=False,
        ),
    ]
