from django.urls import path,include
from .models import Notice
from .views import NoticeListView, FavNoticeView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', NoticeListView)

urlpatterns = [
    path('',include(router.urls)),
    # path('api/details/<int:pk>/', NoticeDetailView.as_view()),
    path('core/fav-notices/', FavNoticeView.as_view())
]