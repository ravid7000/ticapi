# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170408_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Progress'), (2, 'Done')], default=0),
        ),
    ]
