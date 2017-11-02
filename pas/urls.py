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
]