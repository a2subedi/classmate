from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', UserListView)

urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
