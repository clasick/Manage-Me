from django.conf.urls import url

from . import views

app_name = 'pas'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^about/$', views.about, name='about'),
    url(r'^manage-projects/$', views.manage_projects, name='manage_projects'),
    url(r'^manage-employees/$', views.manage_employees, name='manage_employees'),
    url(r'^manage-projects/hide-finished/$', views.manage_hide_finished, name='manage_hide_finished'),
    url(r'^manage-projects/show-overdue/$', views.manage_show_overdue, name='manage_show_overdue'),
    url(r'^manage-groups/$', views.manage_groups, name='manage_groups'),
    url(r'^team/add/$', views.team_add, name='team_add'),
    url(r'^project/add/$', views.project_add, name='project_add'),
    url(r'^employee/add/$', views.employee_add, name='employee_add'),
    url(r'^employee/(?P<employee_id>\d+)/edit/$', views.employee_edit, name='employee_edit'),
    url(r'^project/(?P<project_id>\d+)/edit/$', views.project_edit, name='project_edit'),
    url(r'^team/(?P<team_id>\d+)/edit/$', views.team_edit, name='team_edit'),
    url(r'^team/(?P<team_id>\d+)/delete/$', views.team_delete, name='team_delete'),
    url(r'^resource/(?P<resource_id>\d+)/delete/$', views.resource_delete, name='resource_delete'),
    url(r'^employee/(?P<employee_id>\d+)/delete/$', views.employee_delete, name='employee_delete'),
    url(r'^project/(?P<project_id>\d+)/delete/$', views.project_delete, name='project_delete'),
    url(r'^project/(?P<project_id>\d+)/details/$', views.project_details, name='project_details'),
    url(r'^employee/(?P<employee_id>\d+)/details/$', views.employee_details, name='employee_details'),
    url(r'^team/(?P<team_id>\d+)/details/$', views.team_details, name='team_details'),
    url(r'^panel/(?P<panel_id>\d+)/details/$', views.panel_details, name='panel_details'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^project/(?P<project_id>\d+)/resource/add$', views.resource_add, name='resource_add'),
    url(r'^project/(?P<project_id>\d+)/review/add$', views.review_add, name='review_add'),
    url(r'^panel/(?P<panel_id>\d+)/employees/edit/$', views.panel_edit_employees, name='panel_edit_employees'),
    url(r'^team/(?P<team_id>\d+)/employees/edit/$', views.team_edit_employees, name='team_edit_employees'),
    url(r'^panel/(?P<panel_id>\d+)/edit/$', views.panel_edit, name='panel_edit'),
    url(r'^panel/(?P<panel_id>\d+)/delete/$', views.panel_delete, name='panel_delete'),
    url(r'^panel/add/$', views.panel_add, name='panel_add')
]