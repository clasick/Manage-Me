# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=10)),
                ('join_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.IntegerField(default=0)),
                ('start_date', models.DateField()),
                ('progress', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pas.Team'),
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pas.Team'),
        ),
    ]
