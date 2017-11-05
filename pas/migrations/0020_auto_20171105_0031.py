# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0019_auto_20171104_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='budget',
        ),
        migrations.AlterField(
            model_name='employee',
            name='panel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pas.Panel'),
        ),
    ]
