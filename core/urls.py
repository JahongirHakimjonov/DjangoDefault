from django.conf import settings
from django.conf.urls.i18n import i18n_patterns  # noqa: F401
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .swagger import urlpatterns as swagger_patterns

urlpatterns = [
    path("", include("apps.shared.urls")),
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("rosetta/", include("rosetta.urls")),
]

urlpatterns += swagger_patterns
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
