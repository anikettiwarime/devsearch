from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm, ReviewForm


from .utils import searchProject, paginateProject
# Create your views here.


def projects(request):
    search_query, projects = searchProject(request)
    results = 6
    custom_range, projects = paginateProject(request, projects, results)

    context = {'projects': projects,
               'search_query': search_query, 'custom_range': custom_range}

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()
    tags = projectObj.tags.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount
        messages.success(request, 'Your review has been submited successfully')
        
        return redirect('project', pk=projectObj.id)

    context = {'project': projectObj, 'tags': tags, 'form': form}
    return render(request, 'projects/single-project.html', context)


@login_required(login_url="login")
def addProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,  request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    context = {'object': project}
    print(project)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'delete-template.html', context)
