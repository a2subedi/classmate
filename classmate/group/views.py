from rest_framework import generics,viewsets
from .models import Group

from .serializers import GroupSerializer

class GroupListView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# class GroupDetailView(generics.RetrieveAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
    