# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets_generator', '0005_auto_20160218_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='nutrient_highlight',
            field=models.CharField(choices=[(b'P', b'P'), (b'C', b'C'), (b'G', b'G')], max_length=1),
        ),
    ]
