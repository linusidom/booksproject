# Generated by Django 3.0.5 on 2020-04-20 13:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('chapter', models.IntegerField()),
                ('message', models.TextField(blank=True, null=True)),
                ('create_date', models.DateField(default=datetime.date.today)),
                ('publish_status', models.BooleanField(default=False)),
                ('question_number', models.IntegerField(null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]