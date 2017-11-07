from django import forms
from .models import Team, Project, Employee 
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget 
from django.forms import extras, widgets
import datetime
from datetime import timedelta
from django.core.exceptions import ValidationError
from models import Employee, Team, Project, Panel, Department, Resource, Review

class AddTeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = "__all__" 
	team_name = models.CharField(max_length=20,default='')

class AddProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = "__all__"
	project_name = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '40'}))
	description = forms.CharField(widget=forms.Textarea)
	duration = models.CharField(max_length=20)    
	team = models.ForeignKey(Team)
	panel = models.ForeignKey(Panel)
	start_date = forms.DateField(widget=extras.SelectDateWidget(), label="Start Date (Default - Today) :", initial=datetime.datetime.today())
	percent = models.IntegerField(default=0)
	deadline = forms.DateField(widget=extras.SelectDateWidget(), label="Deadline (Default - 3 Months from Today) :", initial=datetime.datetime.today()+timedelta(90))
		
class AddEmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		exclude = ("team","panel","leader",)
	DESIGNATIONS = (
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
		('Debugger', 'Debugger'),
		('Tester', 'Tester')
    )
	employee_name = models.CharField(max_length=50)
	phone_no = models.CharField(max_length=10)
	designation = forms.ChoiceField(DESIGNATIONS)
	join_date = forms.DateField(widget=extras.SelectDateWidget(years=range(1970, 2017)), label="Join Date (Default - Today) :", initial=datetime.datetime.today())


class AddResourceForm(forms.ModelForm):
	class Meta:
		model = Resource
		exclude = ("project",)
	resource_name = models.CharField(max_length=20)
	amount = models.IntegerField(default=0)

class AddReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		exclude = ("project","panel")
	review_date = forms.SplitDateTimeField(widget=widgets.SplitDateTimeWidget())
	comments = models.CharField(max_length=2000, default='Default Comment')

class AddPanelForm(forms.ModelForm):
	class Meta:
		model = Panel
		fields = "__all__" 