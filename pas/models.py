# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


# Create your models here.    
class Team(models.Model):
    team_name = models.CharField(max_length=20)
    def __str__(self):
        return self.team_name

class Department(models.Model):
    department_name = models.CharField(max_length=20)
    project_budget = models.IntegerField(default=10000)
    def __str__(self):
        return self.department_name

class Panel(models.Model):
    panel_name = models.CharField(max_length=20)
    department = models.ForeignKey(Department)
    def __str__(self):
        return self.panel_name

class Project(models.Model):
    team = models.ForeignKey(Team, null=True, blank=True)
    project_name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, default="")
    start_date = models.DateField(("Start Date"))
    deadline = models.DateField(("Deadline"))
    percent = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    department = models.ForeignKey(Department, null=True)
    panel = models.ForeignKey(Panel, null=True)
    def __str__(self):
        return self.project_name

class Resource(models.Model):
    resource_name = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)
    project = models.ForeignKey(Project, default="")
    def __str__(self):  
        return self.resource_name

class Employee(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number is invalid. Enter up to 10 digits.")
    team = models.ForeignKey(Team, null=True)
    employee_name = models.CharField(max_length=50)
    phone_no =  models.CharField(validators=[phone_regex], max_length=10, blank=True)
    designation = models.CharField(max_length=10, null=True)
    leader = models.BooleanField()
    join_date = models.DateField()
    department = models.ForeignKey(Department, null=True)
    panel = models.ForeignKey(Panel, null=True, blank=True)
    def __str__(self):
        return self.employee_name

class Review(models.Model):    
    project = models.ForeignKey(Project)
    panel = models.ForeignKey(Panel)
    review_date = models.DateTimeField()
    subject = models.CharField(max_length=2000, default="Default Topic", null=True, blank=True)
    comments = models.CharField(max_length=2000, default='Default Comment', null=True, blank=True)
    def get_last_review(self, Project):
        try:
            return Review.objects.filter(project=Project).order_by('-review_date')[0]
        except IndexError:
            pass
    def __str__(self):
        return str(self.project.project_name) + " on " + str(self.review_date)