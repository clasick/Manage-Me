# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
import pytz
from datetime import timedelta
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

# Create your models here.    
class Team(models.Model):
    team_name = models.CharField(max_length=20,default='ANON')
    budget = models.IntegerField(default=0)
    def __str__(self):
        return self.team_name

class Project(models.Model):
    team = models.ForeignKey(Team)
    description = models.CharField(max_length=2000, default="Please describe the project here.")
    start_date = models.DateField(("Start Date"), default=datetime.date.today)
    project_name = models.CharField(max_length=200)
    deadline = models.DateField(("Deadline"), default=datetime.date.today()+timedelta(90))
    percent = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    comments = models.CharField(max_length=2000, default='...')
    def __str__(self):
        return self.project_name

class Employee(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number is invalid. Enter up to 10 digits.")
    team = models.ForeignKey(Team)
    employee_name = models.CharField(max_length=50)
    phone_no =  models.CharField(validators=[phone_regex], max_length=10, blank=True)
    designation = models.CharField(max_length=10)
    join_date = models.DateField()
    def __str__(self):
        return self.employee_name