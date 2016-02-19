# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food_name', models.CharField(max_length=200)),
                ('gr_proteins', models.FloatField()),
                ('gr_carbs', models.FloatField()),
                ('gr_fats', models.FloatField()),
                ('calories', models.FloatField()),
                ('nutrient_highlight', models.CharField(max_length=2)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
