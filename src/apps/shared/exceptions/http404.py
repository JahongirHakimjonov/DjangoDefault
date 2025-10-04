from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError


class Http404Exception(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "not_found"

    def __init__(self, object_name="Object", filters=None):
        filters_text = (
            ", ".join(f"{k}={v}" for k, v in filters.items())
            if filters
            else "given filters"
        )
        detail = {
            "success": False,
            "message": f"{object_name} with {filters_text} not found",
        }
        super().__init__(detail=detail)


def get_object_or_404(object_class, *args, **kwargs):
    """
    Custom get_object_or_404 that raises Http404Exception with JSON detail.
    Example:
        user = get_object_or_404(User, pk=1)
        post = get_object_or_404(Post, slug="my-post")
    """
    try:
        return object_class.objects.get(*args, **kwargs)
    except (object_class.DoesNotExist, ValueError, TypeError, ValidationError):
        # Build filters from kwargs if available, otherwise use args
        filters = kwargs if kwargs else {"args": args}
        raise Http404Exception(object_name=object_class.__name__, filters=filters)
