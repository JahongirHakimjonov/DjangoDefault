from typing import TYPE_CHECKING, Any

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

if TYPE_CHECKING:
    from typing import Protocol

    class AuthUserLike(Protocol):
        is_superuser: bool
        groups: Any


def user_has_group_or_permission(user: "AuthUserLike", permission: str) -> bool:
    if user.is_superuser:
        return True
    if not user.groups.exists():
        return True
    return user.groups.filter(permissions__codename=permission).exists()


PAGES = [
    {
        "seperator": True,
        "items": [
            {
                "title": _("Bosh sahifa"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Foydalanuvchilar"),
        "items": [
            {
                "title": _("Guruhlar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:auth_group_changelist"),
                "permission": lambda request: user_has_group_or_permission(request.user, "view_group"),
            },
            {
                "title": _("Foydalanuvchilar"),
                "icon": "person_add",
                "link": reverse_lazy("admin:users_user_changelist"),
                "permission": lambda request: user_has_group_or_permission(request.user, "view_user"),
            },
        ],
    },
]

TABS = [
    {
        "models": [
            "auth.user",
            "auth.group",
        ],
        "items": [
            {
                "title": _("Foydalanuvchilar"),
                "link": reverse_lazy("admin:auth_user_changelist"),
            },
            {
                "title": _("Guruhlar"),
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
]
