# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post', models.CharField(max_length=140)),
            ],
        ),
    ]