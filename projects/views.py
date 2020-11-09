import random

from django.shortcuts import render
from projects.models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    view = random.random()
    if view >= 0.5:
        return render(request, 'project_index.html', context)
    else:
        return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }

    view = random.random()
    if view >= 0.5:
        return render(request, 'project_detail.html', context)
    else:
        return render(request, 'project_detail.html', context)
