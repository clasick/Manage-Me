# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Team, Project, Employee
from .forms import AddTeamForm, AddProjectForm, AddEmployeeForm
from django.shortcuts import redirect

def index(request):
	all_team_list = Team.objects.all()
	all_employee_list = Employee.objects.all()
	all_project_list = Project.objects.all()
	number1 = len(all_team_list)
	number2 = len(all_employee_list)
	number3 = len(all_project_list)
	context = {'all_team_list': all_team_list, 'all_employee_list': all_employee_list, 'all_project_list': all_project_list, 'number1' : number1, 'number2' : number2, 'number3':number3}
	return render(request, 'pas/index.html', context)

def about(request):
	return render(request, 'pas/about.html')

def manage(request):
	all_team_list = Team.objects.all()
	all_employee_list = Employee.objects.all()
	all_project_list = Project.objects.all()
	number1 = len(all_team_list)
	number2 = len(all_employee_list)
	number3 = len(all_project_list)
	context = {'all_team_list': all_team_list, 'all_employee_list': all_employee_list, 'all_project_list': all_project_list, 'number1' : number1, 'number2' : number2, 'number3':number3}
	return render(request, 'pas/manage.html', context)

def team_add(request):
	if request.method == "POST":
		form = AddTeamForm(request.POST)
		if form.is_valid():
			employee = form.save()
			return redirect('pas:manage')
	else:
		form = AddTeamForm()
	return render(request, 'pas/team_add.html', {'form': form})
	

def project_add(request):
	if request.method == "POST":
		form = AddProjectForm(request.POST)
		if form.is_valid():
			employee = form.save()
			return redirect('pas:manage')
	else:
		form = AddProjectForm()
	return render(request, 'pas/project_add.html', {'form': form})

def employee_add(request):
	if request.method == "POST":
		form = AddEmployeeForm(request.POST)
		if form.is_valid():
			employee = form.save()
			return redirect('pas:manage')
	else:
		form = AddEmployeeForm()
	return render(request, 'pas/employee_add.html', {'form': form})