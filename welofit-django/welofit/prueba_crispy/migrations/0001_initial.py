# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-07 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DietInputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.FloatField()),
                ('proteins_percentage', models.FloatField()),
                ('carbs_percentage', models.FloatField()),
                ('fats_percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('gr_proteins', models.FloatField()),
                ('gr_carbs', models.FloatField()),
                ('gr_fats', models.FloatField()),
                ('calories', models.FloatField()),
                ('food_weight', models.IntegerField()),
                ('nutrient_highlight', models.CharField(choices=[(b'P', b'P'), (b'C', b'C'), (b'G', b'G')], max_length=1)),
            ],
            options={
                'verbose_name': 'Foods',
                'verbose_name_plural': 'Foods',
            },
        ),
    ]