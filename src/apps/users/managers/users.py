from __future__ import annotations

from typing import Any, TypeVar

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager as DjangoUserManager

UserT = TypeVar("UserT", bound=AbstractBaseUser)


class UserManager(DjangoUserManager[UserT]):
    def create_user(
        self,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
        **extra_fields: Any,
    ) -> UserT:
        extra_fields.setdefault("is_active", True)
        if email is None:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)

        user: UserT = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
        **extra_fields: Any,
    ) -> UserT:
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username=username, email=email, password=password, **extra_fields)
