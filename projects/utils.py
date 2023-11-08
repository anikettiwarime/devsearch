from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Tag, Project
from django.db.models import Q


def paginateProject(request, projects, results):

    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page)-4)

    if leftIndex <= 0:
        leftIndex = 1

    righttIndex = (int(page)+5)

    if righttIndex >= paginator.num_pages:
        righttIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, righttIndex)
    return custom_range, projects


def searchProject(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return search_query, projects
