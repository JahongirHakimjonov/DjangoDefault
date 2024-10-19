from django.contrib.auth.decorators import login_required
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path(
        "schema/",
        login_required(SpectacularAPIView.as_view(), login_url="/admin/"),
        name="schema",
    ),
    path(
        "api/schema/swagger-ui/",
        login_required(
            SpectacularSwaggerView.as_view(url_name="schema"), login_url="/admin/"
        ),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        login_required(
            SpectacularRedocView.as_view(url_name="schema"), login_url="/admin/"
        ),
        name="redoc",
    ),
]
