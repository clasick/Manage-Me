from django import forms
from .models import Team, Project, Employee 
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget 
from django.forms import extras
import datetime
from datetime import timedelta
from django.core.exceptions import ValidationError
from models import Employee, Team, Project


class AddTeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = "__all__" 
	team_name = models.CharField(max_length=20,default='')
	budget = models.IntegerField(default=0)

class AddProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ("team",)
	project_name = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '40'}))
	description = forms.CharField(widget=forms.Textarea)
	duration = models.CharField(max_length=20)
	start_date = forms.DateField(widget=extras.SelectDateWidget(), label="Start Date (Default - Today) :", initial=datetime.datetime.today())
	percent = models.IntegerField(default=0)
	deadline = forms.DateField(widget=extras.SelectDateWidget(), label="Deadline (Default - 3 Months from Today) :", initial=datetime.datetime.today()+timedelta(90))
	comments = forms.CharField(widget=forms.Textarea)
	
class AddEmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		exclude = ("team",)
	DESIGNATIONS = (
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
		('Debugger', 'Debugger'),
		('Tester', 'Tester'),
    )
	employee_name = models.CharField(max_length=50)
	phone_no = models.CharField(max_length=10)
	designation = forms.ChoiceField(DESIGNATIONS)
	leader =  forms.BooleanField(required=False, initial=False)
	join_date = forms.DateField(widget=extras.SelectDateWidget(), label="Join Date (Default - Today) :", initial=datetime.datetime.today())


