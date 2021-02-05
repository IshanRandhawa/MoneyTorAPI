from rest_framework import viewsets, permissions
from .serializers import serverSerializer
from .models import server


class LeadViewSet(viewsets.ModelViewSet):
    queryset = server.objects.all()
    serializer_class = serverSerializer
