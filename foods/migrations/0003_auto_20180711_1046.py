# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-11 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_food_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_user', to='accounts.UserModel'),
        ),
    ]
