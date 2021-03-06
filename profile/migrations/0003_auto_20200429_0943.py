# Generated by Django 3.0.5 on 2020-04-29 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile', '0002_auto_20200424_0449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, primary_key=True, related_name='user_profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
