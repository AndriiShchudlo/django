# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.TextField()),
                ('foodImage', models.TextField(default=None)),
            ],
            options={
                'db_table': 'food',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.TextField()),
                ('categoryPrice', models.FloatField()),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.AddField(
            model_name='food',
            name='foodCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinner.Menu'),
        ),
    ]