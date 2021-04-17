
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('api/notices/', include('notice.urls')),
    path('api/groups/', include('group.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
]
