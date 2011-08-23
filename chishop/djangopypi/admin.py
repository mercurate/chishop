from django.contrib import admin
from chishop.djangopypi.models import Project, Release, Classifier

admin.site.register(Project)
admin.site.register(Release)
admin.site.register(Classifier)
