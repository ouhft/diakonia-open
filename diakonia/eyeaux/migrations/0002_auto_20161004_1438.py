# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyeaux', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhsbtrecord',
            name='_psuedo_id_d',
            field=models.CharField(blank=True, db_index=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='nhsbtrecord',
            name='_psuedo_id_r',
            field=models.CharField(blank=True, db_index=True, default='', max_length=10),
        ),
    ]
