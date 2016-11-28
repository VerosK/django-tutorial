# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=96, verbose_name='Otazka')),
                ('is_active', models.BooleanField(default=True, verbose_name='Je aktivni')),
            ],
        ),
    ]