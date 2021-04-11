from django.urls import path
from .models import Notice
from .views import NoticeListView, NoticeDetailView

urlpatterns = [
    path('api/', NoticeListView.as_view()),
    path('api/<int:pk>/', NoticeDetailView.as_view()),
]