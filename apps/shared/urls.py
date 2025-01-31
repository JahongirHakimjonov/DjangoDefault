from django.urls import path

from apps.shared.views.base import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
