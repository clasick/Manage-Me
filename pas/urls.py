from django.conf.urls import url

from . import views

app_name = 'pas'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^manage/$', views.manage, name='manage'),
    url(r'^about/$', views.about, name='about'),
    url(r'^team/add/$', views.team_add, name='team_add'),
    url(r'^project/add/$', views.project_add, name='project_add'),
    url(r'^employee/add/$', views.employee_add, name='employee_add'),
    url(r'^employee/(?P<employee_id>\d+)/edit/$', views.employee_edit, name='employee_edit'),
    url(r'^project/(?P<project_id>\d+)/edit/$', views.project_edit, name='project_edit'),
    url(r'^team/(?P<team_id>\d+)/edit/$', views.team_edit, name='team_edit'),
    url(r'^team/(?P<team_id>\d+)/delete/$', views.team_delete, name='team_delete'),
    url(r'^employee/(?P<employee_id>\d+)/delete/$', views.employee_delete, name='employee_delete'),
    url(r'^project/(?P<project_id>\d+)/delete/$', views.project_delete, name='project_delete')
]