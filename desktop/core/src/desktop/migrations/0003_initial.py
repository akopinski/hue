# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-13 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('desktop', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('desktop.document2',),
        ),
    ]