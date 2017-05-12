# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.TextField()),
                ('foodDescriptions', models.TextField()),
                ('foodImage', models.TextField(default=None)),
                ('foodCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinner.Menu')),
                ('foodDay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinner.FoodDay')),
            ],
            options={
                'db_table': 'eating',
            },
        ),
        migrations.RemoveField(
            model_name='foods',
            name='foodCategory',
        ),
        migrations.RemoveField(
            model_name='foods',
            name='foodDay',
        ),
        migrations.DeleteModel(
            name='Foods',
        ),
    ]
