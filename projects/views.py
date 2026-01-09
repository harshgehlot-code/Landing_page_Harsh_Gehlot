from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer


class ProjectListView(generics.ListAPIView):
    """
    GET /api/projects/
    Returns a list of all projects
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
