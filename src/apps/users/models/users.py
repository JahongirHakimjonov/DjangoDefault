from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from apps.shared.models.base import AbstractBaseModel
from apps.users.managers.users import UserManager


class RoleChoices(models.TextChoices):
    ADMIN = "ADMIN", _("Admin")
    USER = "USER", _("User")
    MODERATOR = "MODERATOR", _("Moderator")


class User(AbstractUser, AbstractBaseModel):
    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True,
        db_index=True,
    )
    username = models.CharField(
        max_length=100,
        verbose_name=_("Username"),
        db_index=True,
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True,
        blank=True,
        verbose_name=_("Avatar"),
        db_index=True,
    )
    role = models.CharField(
        choices=RoleChoices.choices,
        max_length=20,
        default=RoleChoices.USER,
        verbose_name=_("Role"),
        db_index=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}" if self.email else str(_("User"))

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-created_at"]
        db_table = "users"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": self.id,
        }
