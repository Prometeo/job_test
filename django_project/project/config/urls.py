from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views import defaults as default_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("users/", include("apps.users.urls", namespace="users")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    path("api/", include("config.api_router")),
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += []
