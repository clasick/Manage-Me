# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.    
class Team(models.Model):
    team_name = models.CharField(max_length=20,default='ANON')
    budget = models.IntegerField(default=0)
    start_date = models.DateField()
    progress = models.CharField(max_length=2000)
    def __str__(self):
        return self.team_name

class Project(models.Model):
    team = models.ForeignKey(Team)
    project_name = models.CharField(max_length=200)
    duration = models.CharField(max_length=20)
    def __str__(self):
        return self.project_name

class Employee(models.Model):
    team = models.ForeignKey(Team)
    employee_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    designation = models.CharField(max_length=10)
    join_date = models.DateField()
    def __str__(self):
        return self.employee_name