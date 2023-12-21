from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, 'projects/list_projects.html', context)

@login_required
def show_project(request, id):
    project = Project.objects.get(id=id)
    context = {
        "project": project,
    }
    return render(request, "projects/show_project.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
            return redirect("list_projects")
    else:
        project_form = ProjectForm()
    context = {"project_form": project_form}
    return render(request, "projects/create_project.html", context)
