import os
import shutil
import subprocess

from django.template import RequestContext
from django.shortcuts import redirect
from django.db.models.query import Q

from chishop.djangopypi.models import Project, UPLOAD_TO

from chishop.djangopypi.forms import ProjectForm, ReleaseForm, UploadForm

import settings


def upload(request):
    if request.method != 'POST':
        return redirect('/')

    form = UploadForm(request.POST, request.FILES)
    if not form.is_valid():
        return redirect('/')

    package = request.FILES['package']
    if not os.path.exists(settings.UPLOAD):
        os.makedirs(settings.UPLOAD)
    pkg_path = os.path.join(settings.UPLOAD, package.name)
    if os.path.exists(pkg_path):
        return redirect('/')

    f = open(pkg_path, 'wb+')
    for chunk in package.chunks():
        f.write(chunk)
    f.close()

    if not pkg_path.endswith(('.tar.gz', '.tgz')):
        return redirect('/')

    c = 'tar -xzf %s' % (pkg_path)
    subprocess.check_call(c.split(), cwd = settings.UPLOAD)
    cmd = 'python setup.py register -r local sdist upload -r local'
    for name in os.listdir(settings.UPLOAD):
        path = os.path.join(settings.UPLOAD, name)
        if not os.path.isdir(path):
            continue
        setup_file = os.path.join(path, 'setup.py')
        if os.path.exists(setup_file):
            print cmd, path
            subprocess.call(cmd.split(), cwd = path)
        shutil.rmtree(path)

    return redirect('/')
