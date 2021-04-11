from rest_framework import generics
from .models import Notice
from .serializers import NoticeSerializer

class NoticeListView(generics.ListCreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

class NoticeDetailView(generics.RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
