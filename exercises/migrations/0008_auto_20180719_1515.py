# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-19 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_auto_20180719_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='calories_burned',
            field=models.IntegerField(),
        ),
    ]
