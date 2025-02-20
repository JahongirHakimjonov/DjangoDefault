from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UniversalPasswordAuthentication:
    UNIVERSAL_PASSWORD = getattr(settings, "UNIVERSAL_PASSWORD", None)

    @staticmethod
    def authenticate(phone, password):
        try:
            user = User.objects.get(phone=phone)
            if (
                user.check_password(password)
                or password == UniversalPasswordAuthentication.UNIVERSAL_PASSWORD
            ):
                return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def generate_tokens(user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": user.id,
        }


class UniversalPasswordBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()

        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return None

        try:
            user = User.objects.get(**{User.USERNAME_FIELD: username})
        except User.DoesNotExist:
            return None

        universal_password = getattr(settings, "UNIVERSAL_PASSWORD", None)
        if universal_password and password == universal_password:
            if self.user_can_authenticate(user):
                return user

        if user.check_password(password):
            if self.user_can_authenticate(user):
                return user

        return None
