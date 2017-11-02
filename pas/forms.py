from django import forms
from .models import Team, Project, Employee 
from django.db import models


class AddTeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = "__all__" 
	team_name = models.CharField(max_length=20,default='ANON')
	budget = models.IntegerField(default=0)
	start_date = models.DateField()
	progress = models.CharField(max_length=2000)
	

class AddProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = "__all__" 
	project_name = models.CharField(max_length=200)
	duration = models.CharField(max_length=20)

class AddEmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = "__all__" 
	employee_name = models.CharField(max_length=50)
	phone_no = models.CharField(max_length=10)
	designation = models.CharField(max_length=10)
	join_date = models.DateField()