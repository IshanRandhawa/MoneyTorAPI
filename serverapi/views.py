from rest_framework import views, viewsets, permissions, authentication
from .serializers import serverSerializer
from .models import server


class LeadViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = server.objects.all()
    serializer_class = serverSerializer
    permission_classes = [permissions.IsCanViewOnly]

