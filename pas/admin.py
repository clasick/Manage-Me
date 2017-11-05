# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Team, Project, Employee, Department, Review, Resource, Panel

admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Review)
admin.site.register(Resource)
admin.site.register(Panel)