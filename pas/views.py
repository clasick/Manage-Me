# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Team, Project, Employee
from .forms import AddTeamForm, AddProjectForm, AddEmployeeForm
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.timezone import localtime, now


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

def dashboard(request):
	all_team_list = Team.objects.all()
	today = timezone.now()
	count = 0
	finished = 0
	on_schedule = 0 
	overdue = 0
	for project in Project.objects.all():
		count += 1
		if project.percent >= 100:
			finished += 1
		elif (localtime(now()).date() > project.deadline) and (project.percent < 100):
			overdue += 1
		else:
			on_schedule += 1
	finished = finished/count * 100
	overdue = overdue/count * 100
	on_schedule = on_schedule/count * 100
	context = {'all_team_list': all_team_list, 'date': today, 'project_count': count, 'project_finished': finished, 'project_on_schedule': on_schedule, 'project_overdue': overdue}
	return render(request, 'pas/dashboard.html', context)

def manage(request):
	all_team_list = Team.objects.all()
	context = {'all_team_list': all_team_list}
	return render(request, 'pas/manage.html', context)

def manage_hide_finished(request):
	all_team_list = Team.objects.all()
	finished_list = []
	for team in all_team_list:
		if team.project_set.all()[0].percent < 100:
			finished_list.append(team)
	context = {'all_team_list': finished_list}
	return render(request, 'pas/manage.html', context)

def manage_show_overdue(request):
	all_team_list = Team.objects.all()
	overdue_list = []
	for team in all_team_list:
		if (localtime(now()).date() > team.project_set.all()[0].deadline) and (team.project_set.all()[0].percent < 100):
			overdue_list.append(team)
	context = {'all_team_list': overdue_list}
	return render(request, 'pas/manage.html', context)

def team_add(request):
	if request.method == "POST":
		form = AddTeamForm(request.POST)
		if form.is_valid():
			team = form.save()
			return redirect('pas:manage')
	else:
		form = AddTeamForm()
	return render(request, 'pas/team_add.html', {'form': form})
	

def project_add(request, team_id):
	if request.method == "POST":
		form = AddProjectForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			project.team_id = team_id
			project.save()
			return redirect('pas:team_details', project.team_id)
	else:
		form = AddProjectForm()
	return render(request, 'pas/project_add.html', {'form': form})

def employee_add(request, team_id):
	if request.method == "POST":
		form = AddEmployeeForm(request.POST)
		if form.is_valid():
			employee = form.save(commit=False)
			employee.team_id = team_id
			employee.save()
			return redirect('pas:team_details', employee.team_id)
	else:
			form = AddEmployeeForm()
	return render(request, 'pas/employee_add.html', {'form': form})

def employee_edit(request, employee_id):
	employee = get_object_or_404(Employee, pk=employee_id)
	if request.method == "POST":
		form = AddEmployeeForm(request.POST, instance=employee)
		if form.is_valid():
			employee = form.save()
			return redirect('pas:team_details', employee.team_id)
	else:
		form = AddEmployeeForm(instance=employee)
	return render(request, 'pas/employee_edit.html', {'form': form})

def project_edit(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	if request.method == "POST":
		form = AddProjectForm(request.POST, instance=project)
		if form.is_valid():
			project = form.save()
			return redirect('pas:team_details', project.team_id)
	else:
		form = AddProjectForm(instance=project)
	return render(request, 'pas/project_edit.html', {'form': form})

def team_edit(request, team_id):
	team = get_object_or_404(Team, pk=team_id)
	if request.method == "POST":
		form = AddTeamForm(request.POST, instance=team)
		if form.is_valid():
			team = form.save()
			return redirect('pas:team_details', team.id)
	else:
		form = AddTeamForm(instance=team)
	return render(request, 'pas/team_edit.html', {'form': form})
	
def team_delete(request, team_id):
    Team.objects.get(pk=team_id).delete()
    return redirect('pas:manage')

def employee_delete(request, employee_id):
	e = Employee.objects.get(pk=employee_id)
	team_id = e.team_id
	e.delete()
	return redirect('pas:team_details', team_id)

def project_delete(request, project_id):
    p = Project.objects.get(pk=project_id)
    team_id = p.team_id
    p.delete()
    return redirect('pas:team_details', team_id)

def team_details(request, team_id):
	team = get_object_or_404(Team, pk=team_id)
	context = {'team' : team}
	return render(request, 'pas/team_details.html', context)