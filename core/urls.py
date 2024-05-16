from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .swagger import urlpatterns as swagger_patterns
from core import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.shared.urls")),
]
urlpatterns += swagger_patterns
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
