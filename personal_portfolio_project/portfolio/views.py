from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/detail.html', {'project': project})