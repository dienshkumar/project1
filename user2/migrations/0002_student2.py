# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auther_name', models.CharField(max_length=200)),
                ('address_name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(max_length=100)),
            ],
        ),
    ]
