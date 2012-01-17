import os
import shutil
import subprocess

from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.db.models.query import Q

from chishop.djangopypi.models import Project

from chishop.djangopypi.forms import ProjectForm, ReleaseForm, UploadForm

def upload(request):
    if request.method == 'GET':
        return render(request, 'djangopypi/upload.html', {'form': UploadForm()})

    print 'upload starts!'
    form = UploadForm(request.POST, request.FILES)
    if not form.is_valid():
        print 'not valid...'
        return render(request, 'djangopypi/upload.html', {'form': form})

    package = request.FILES['package']
    if not os.path.exists(settings.UPLOAD):
        print 'create dir %s', settings.UPLOAD
        os.makedirs(settings.UPLOAD)
    pkg_path = os.path.join(settings.UPLOAD, package.name)
    if os.path.exists(pkg_path):
        print '%s exists, skip save.' % pkg_path
    else:
        f = open(pkg_path, 'wb+')
        for chunk in package.chunks():
            f.write(chunk)
        f.close()

    if not pkg_path.endswith(('.tar.gz', '.tgz')):
        print 'not a tar.gz'
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

    print 'upload done'
    return redirect('/')
