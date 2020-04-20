# Generated by Django 3.0.5 on 2020-04-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('artist', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('occurrences', models.IntegerField(blank=True, null=True)),
                ('wikilink', models.CharField(blank=True, max_length=255, null=True)),
                ('amazonlink', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
