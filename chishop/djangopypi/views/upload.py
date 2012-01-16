import os

from django.template import RequestContext
from django.shortcuts import redirect
from django.db.models.query import Q

from chishop.djangopypi.models import Project, UPLOAD_TO

from chishop.djangopypi.forms import ProjectForm, ReleaseForm, UploadForm

import settings


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            package = request.FILES['package']
            if not os.path.exists(settings.UPLOAD):
                os.makedirs(settings.UPLOAD)
            path = os.path.join(settings.UPLOAD, package.name)
            print 'saving file to', path
            f = open(path, 'wb+')
            for chunk in package.chunks():
                f.write(chunk)
            f.close()
    return redirect('/')
