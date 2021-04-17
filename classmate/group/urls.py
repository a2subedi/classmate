from django.urls import path,include
from .views import GroupListView, join_group
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', GroupListView)

urlpatterns = [
    path('',include(router.urls)),
    # path('api/details/<int:pk>/', NoticeDetailView.as_view()),
    path('/api/join-group/', join_group)
]