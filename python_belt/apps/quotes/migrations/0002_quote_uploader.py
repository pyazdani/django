# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded', to='login.User'),
            preserve_default=False,
        ),
    ]
