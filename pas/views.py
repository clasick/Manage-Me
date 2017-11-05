# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Team, Project, Employee, Resource, Review, Panel
from .forms import AddTeamForm, AddProjectForm, AddEmployeeForm, AddResourceForm, AddReviewForm
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.timezone import localtime, now
from django.contrib.auth import logout
import operator
from django.views.generic import ListView

from django.db.models import Q

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
	if request.user.is_authenticated():
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
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)

def manage_projects(request):
	if request.user.is_authenticated():
		project_list = Project.objects.all()
		context = {'project_list': project_list}
		return render(request, 'pas/manage-projects.html', context)
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)

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
	if request.user.is_authenticated():
		if request.method == "POST":
			form = AddTeamForm(request.POST)
			if form.is_valid():
				team = form.save()
				return redirect('pas:manage')
		else:
			form = AddTeamForm()
		return render(request, 'pas/team_add.html', {'form': form})
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)
	

def project_add(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = AddProjectForm(request.POST)
			if form.is_valid():
				project = form.save(commit=False)
				project.save()
				return redirect('pas:project_details')
		else:
			form = AddProjectForm()
		return render(request, 'pas/project_add.html', {'form': form})
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)

def employee_add(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = AddEmployeeForm(request.POST)
			if form.is_valid():
				employee = form.save(commit=False)
				employee.save()
				return redirect('pas:manage_employees')
		else:
				form = AddEmployeeForm()
		return render(request, 'pas/employee_add.html', {'form': form})
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)

def employee_edit(request, employee_id):
	if request.user.is_authenticated():
		employee = get_object_or_404(Employee, pk=employee_id)
		if request.method == "POST":
			form = AddEmployeeForm(request.POST, instance=employee)
			if form.is_valid():
				employee = form.save()
				return redirect('pas:project_details', employee.team_id)
		else:
			form = AddEmployeeForm(instance=employee)
		return render(request, 'pas/employee_edit.html', {'form': form})
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)

def project_edit(request, project_id):
	if request.user.is_authenticated():
		project = get_object_or_404(Project, pk=project_id)
		if request.method == "POST":
			form = AddProjectForm(request.POST, instance=project)
			if form.is_valid():
				project = form.save()
				return redirect('pas:project_details', project.id)
		else:
			form = AddProjectForm(instance=project)
		return render(request, 'pas/project_edit.html', {'form': form})
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)

def team_edit(request, team_id):
	if request.user.is_authenticated():
		team = get_object_or_404(Team, pk=team_id)
		if request.method == "POST":
			form = AddTeamForm(request.POST, instance=team)
			if form.is_valid():
				team = form.save()
				return redirect('pas:project_details', team.id)
		else:
			form = AddTeamForm(instance=team)
		return render(request, 'pas/team_edit.html', {'form': form})
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)
	
def team_delete(request, team_id):
    Team.objects.get(pk=team_id).delete()
    return redirect('pas:manage')

def employee_delete(request, employee_id):
	e = Employee.objects.get(pk=employee_id)
	team_id = e.team_id
	e.delete()
	return redirect('pas:project_details', team_id)

def project_delete(request, project_id):
    p = Project.objects.get(pk=project_id)
    team_id = p.team_id
    p.delete()
    return redirect('pas:project_details', team_id)

def project_details(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	review_list = Review.objects.filter(project=project)
	resource_list = Resource.objects.all()
	last = Review().get_last_review(project)
	today = localtime(now())
	total = 0
	limit = project.department.project_budget
	for resource in resource_list:
		total += resource.amount 
	context = {'project' : project, 'resource_list':resource_list, 'review_list':review_list, 'today':today, 'last':last, 'total':total, 'limit':limit}
	return render(request, 'pas/project_details.html', context)

def team_details(request, team_id):
	team = get_object_or_404(Team, pk=team_id)
	context = {'team': team}
	return render(request, 'pas/team_details.html', context)

def panel_details(request, panel_id):
	panel = get_object_or_404(Panel, pk=panel_id)
	context = {'panel': panel}
	return render(request, 'pas/panel_details.html', context)

def user_logout(request):
	if request.user.is_authenticated():
		logout(request)
		loggedout = 'You are have been logged out!'
		context = {'loggedout':loggedout}
		return render(request, 'pas/index.html', context)
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)

def show_employees(request):
	employees = Employee.objects.all()
	my_string = "hello this is my string"
	context = {'employees': employees}
	return render(request, 'pas/employees.html', context)

def manage_groups(request):
	if request.user.is_authenticated():
		team_list = Team.objects.all()
		panel_list = Panel.objects.all()
		project_list = []
		panel_project_list = []
		for team in team_list:
			project_list.append(Project.objects.filter(team=team).first())
		for panel in panel_list:
			panel_project_list.append(Project.objects.filter(panel=panel).first())
		panel_list = zip(panel_list, panel_project_list)
		team_list = zip(team_list, project_list)
		context = {'team_list':team_list, 'panel_list':panel_list, 'project_list':project_list}
		return render(request, 'pas/manage-groups.html', context)
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)

def resource_add(request, project_id):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = AddResourceForm(request.POST)
			if form.is_valid():
				resource = form.save(commit=False)
				if project_id:
					resource.project_id = project_id
				resource.save()
				if project_id:
					return redirect('pas:project_details', resource.project_id)
				else:
					return redirect('pas:team_details', team_id)
		else:
				form = AddResourceForm()
		return render(request, 'pas/resource_add.html', {'form': form})
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)

def review_add(request, project_id):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = AddReviewForm(request.POST)
			if form.is_valid():
				review = form.save(commit=False)
				if project_id:
					review.project_id = project_id
					review.panel_id = Project.objects.get(pk=project_id).panel_id
				review.save()
				if project_id:
					return redirect('pas:project_details', review.project_id)
				else:
					return redirect('pas:team_details', team_id)
		else: 
				form = AddReviewForm()
		return render(request, 'pas/review_add.html', {'form': form})
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)

def panel_add_employee(request, panel_id):
	if request.user.is_authenticated():
		if request.method == 'POST': 
			employee_list = request.POST.getlist('employees')
			for employee_id in employee_list:
				e = Employee.objects.get(pk=employee_id)
				e.panel_id = panel_id
				e.save()
			return redirect('pas:panel_details', panel_id)
		else:
			employee_list = Employee.objects.filter(panel=None, department=Panel.objects.get(pk=panel_id).department)
			context = {'employee_list': employee_list} 
			return render(request, 'pas/panel_add_employee.html', context)
	else:
		error = "You do not have permission to access this page. Please log in and try again."
		context = {'login_error': error}
		return render(request, 'pas/index.html', context)