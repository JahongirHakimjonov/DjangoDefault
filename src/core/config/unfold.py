from django.conf import settings
from django.http import HttpRequest
from django.templatetags.static import static
from django.utils.functional import Promise
from django.utils.translation import gettext_lazy as _

from . import unfold_navigation as navigation


def environment_callback(request: HttpRequest) -> list[str | Promise]:
    label: str | Promise = _("Development") if settings.DEBUG else _("Production")
    return [label, "primary"]


UNFOLD = {
    "SITE_TITLE": "Django Default",
    "SITE_HEADER": "Django Default",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("images/django-logo.webp"),
        "dark": lambda request: static("images/django-logo.webp"),
    },
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/icon",
            "href": lambda request: static("images/favicon.ico"),
        },
    ],
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_LANGUAGES": True,
    "SHOW_BACK_BUTTON": True,
    "ENVIRONMENT": "core.config.unfold.environment_callback",
    "LOGIN": {
        "image": lambda request: static("images/purple.jpg"),
    },
    "BORDER_RADIUS": "10px",
    "COLORS": {
        "base": {
            "50": "oklch(0.98 0.002 270)",
            "100": "oklch(0.96 0.003 270)",
            "200": "oklch(0.91 0.004 270)",
            "300": "oklch(0.85 0.006 270)",
            "400": "oklch(0.70 0.010 270)",
            "500": "oklch(0.55 0.013 270)",
            "600": "oklch(0.44 0.015 270)",
            "700": "oklch(0.36 0.013 270)",
            "800": "oklch(0.26 0.010 270)",
            "900": "oklch(0.18 0.008 270)",
            "950": "oklch(0.10 0.006 270)",
        },
        "primary": {
            "50": "oklch(0.97 0.015 290)",
            "100": "oklch(0.94 0.027 290)",
            "200": "oklch(0.88 0.045 290)",
            "300": "oklch(0.80 0.070 290)",
            "400": "oklch(0.73 0.095 290)",
            "500": "oklch(0.66 0.115 290)",
            "600": "oklch(0.59 0.130 290)",
            "700": "oklch(0.51 0.125 290)",
            "800": "oklch(0.43 0.110 290)",
            "900": "oklch(0.37 0.090 290)",
            "950": "oklch(0.28 0.060 290)",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",  # text-base-500
            "subtle-dark": "var(--color-base-400)",  # text-base-400
            "default-light": "var(--color-base-600)",  # text-base-600
            "default-dark": "var(--color-base-300)",  # text-base-300
            "important-light": "var(--color-base-900)",  # text-base-900
            "important-dark": "var(--color-base-100)",  # text-base-100
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "uz": "🇺🇿",
                "ru": "🇷🇺",
                "en": "🇬🇧",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": navigation.PAGES,
    },
    # "TABS": navigation.TABS,
}
