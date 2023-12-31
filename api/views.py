from rest_framework.response import Response
from rest_framework.decorators import api_view
from projects.models import Project
from .serializers import ProjectSerializer
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'projects/'},
        {'GET': 'projects/id'},
        {'POST': 'projects/id'},
        {'GET': 'projects/id'},
    ]

    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
