from __future__ import annotations

from collections.abc import Callable
from typing import Any, ParamSpec, TypeVar

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.templatetags.static import static
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RangeDateFilter
from unfold.decorators import display
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from apps.users.models.users import RoleChoices, User

P = ParamSpec("P")
R = TypeVar("R")


def typed_display(*d_args: Any, **d_kwargs: Any) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def _outer(func: Callable[P, R]) -> Callable[P, R]:
        return display(*d_args, **d_kwargs)(func)  # type: ignore[misc]

    return _outer


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):  # type:ignore[misc]
    change_password_form = AdminPasswordChangeForm
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ("avatars", "username", "show_role_customized_color", "is_active")
    search_fields = ("email", "username", "first_name", "last_name")
    list_filter = (
        "role",
        "is_active",
        ("created_at", RangeDateFilter),
    )
    list_editable = ("is_active",)
    list_display_links = ("username", "avatars")
    list_filter_submit = True
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "avatar",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "role",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    @typed_display(
        description="Role",
        ordering="role",
        label={
            RoleChoices.ADMIN: "success",
            RoleChoices.MODERATOR: "info",
            RoleChoices.USER: "info",
        },
    )
    def show_role_customized_color(self, obj: User) -> tuple[str, str]:
        return obj.role, obj.get_role_display()

    @typed_display(header=True)
    def avatars(self, obj: User) -> list[Any]:
        return [
            f"{obj.first_name} {obj.last_name}",
            f"ID:{obj.id} - {obj.email}",
            "AB",
            {
                "path": obj.avatar.url if obj.avatar else static("images/avatar.webp"),
                "squared": False,
                "borderless": True,
                "width": 50,
                "height": 50,
            },
        ]
