from django.urls import path,include
from .views import GroupListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', GroupListView)

urlpatterns = [
    path('',include(router.urls)),
    # path('api/details/<int:pk>/', NoticeDetailView.as_view()),
]