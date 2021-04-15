from rest_framework import generics,viewsets
from .models import Notice
from .serializers import NoticeSerializer

class NoticeListView(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

# class NoticeDetailView(generics.RetrieveAPIView):
#     queryset = Notice.objects.all()
#     serializer_class = NoticeSerializer
