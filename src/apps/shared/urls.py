from django.conf import settings
from django.urls import path

from apps.shared.views.base import HomeView

urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        path("", HomeView.as_view(), name="home"),
    ]
