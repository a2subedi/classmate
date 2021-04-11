from django.urls import path
from .views import GroupListView, GroupDetailView

urlpatterns = [
    path('api/', GroupListView.as_view()),
    path('api/<int:pk>/', GroupDetailView.as_view()),
]