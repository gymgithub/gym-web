# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diets_generator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietInputs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calories', models.FloatField()),
                ('proteins_percentage', models.FloatField()),
                ('carbs_percentage', models.FloatField()),
                ('fats_percentage', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='foods',
            old_name='value',
            new_name='food_weight',
        ),
    ]
