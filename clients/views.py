from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer


class ClientListView(generics.ListAPIView):
    """
    GET /api/clients/
    Returns a list of all clients
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
