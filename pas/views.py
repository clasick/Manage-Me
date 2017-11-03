# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Team, Project, Employee
from .forms import AddTeamForm, AddProjectForm, AddEmployeeForm
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

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

def employee_edit(request, employee_id):
	employee = get_object_or_404(Employee, pk=employee_id)
	if request.method == "POST":
		form = AddEmployeeForm(request.POST, instance=employee)
		if form.is_valid():
			employee = form.save()
			return redirect('pas:manage')
	else:
		form = AddEmployeeForm(instance=employee)
	return render(request, 'pas/employee_edit.html', {'form': form})

def project_edit(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if request.method == "POST":
		form = AddProjectForm(request.POST, instance=project)
		if form.is_valid():
			project = form.save()
			return redirect('pas:manage')
	else:
		form = AddProjectForm(instance=project)
	return render(request, 'pas/project_edit.html', {'form': form})

def team_edit(request, team_id):
	team = get_object_or_404(Team, pk=team_id)
	if request.method == "POST":
		form = AddTeamForm(request.POST, instance=team)
		if form.is_valid():
			team = form.save()
			return redirect('pas:manage')
	else:
		form = AddTeamForm(instance=team)
	return render(request, 'pas/team_edit.html', {'form': form})

def team_delete(request, team_id):
   Team.objects.get(pk=team_id).delete()
   return redirect('pas:manage')

def employee_delete(request, employee_id):
   employee.objects.get(pk=employee_id).delete()
   return redirect('pas:manage')

def project_delete(request, project_id):
   project.objects.get(pk=project_id).delete()
   return redirect('pas:manage')