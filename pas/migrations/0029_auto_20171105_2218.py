# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 16:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0028_department_budget'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='budget',
            new_name='project_budget',
        ),
    ]
