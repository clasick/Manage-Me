# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0017_employee_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='leader',
            field=models.BooleanField(),
        ),
    ]
