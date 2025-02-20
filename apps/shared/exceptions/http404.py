from rest_framework.exceptions import APIException


class Http404Exception(APIException):
    status_code = 404
    default_code = "not_found"

    def __init__(self, object_name="Object", pk=None):
        self.detail = {
            "success": False,
            "message": f"{object_name} with {pk} pk not found",
        }


def get_object_or_404(object_class, pk):
    try:
        return object_class.objects.get(pk=pk)
    except (object_class.DoesNotExist, ValueError, TypeError):
        raise Http404Exception(object_class.__name__, pk)
