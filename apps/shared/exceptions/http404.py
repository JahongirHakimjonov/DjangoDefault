from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError


class Http404Exception(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "not_found"

    def __init__(self, object_name="Object", pk=None):
        self.detail = {
            "success": False,
            "message": f"{object_name} with {pk} pk not found",
        }


def get_object_or_404(object_class, pk, *args, **kwargs):
    try:
        return object_class.objects.get(pk=pk, *args, **kwargs)
    except (object_class.DoesNotExist, ValueError, TypeError, ValidationError):
        raise Http404Exception(object_class.__name__, pk)
