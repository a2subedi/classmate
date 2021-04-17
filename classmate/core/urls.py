from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserListView
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
# from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Suchana API'
API_DESCRIPTION = 'A Web API for creating and editing Suchanas.'
schema_view = get_swagger_view(title=API_TITLE)

router = routers.DefaultRouter()
router.register('users', UserListView)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('docs/', include_docs_urls(title='Suchana API')),
    path('swagger-docs/', schema_view),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
