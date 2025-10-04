from __future__ import annotations

from typing import Any, Protocol, TypeVar, runtime_checkable

from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError


@runtime_checkable
class ModelLike(Protocol):
    objects: Any
    DoesNotExist: type[Exception]


T = TypeVar("T", bound=ModelLike)


class Http404Exception(APIException):  # type:ignore[misc]
    status_code: int = status.HTTP_404_NOT_FOUND
    default_code: str = "not_found"

    def __init__(self, object_name: str = "Object", filters: dict[str, Any] | None = None) -> None:
        filters_text = ", ".join(f"{k}={v}" for k, v in filters.items()) if filters else "given filters"
        detail: dict[str, Any] = {
            "success": False,
            "message": f"{object_name} with {filters_text} not found",
        }
        super().__init__(detail=detail)


def get_object_or_404(object_class: type[T], *args: Any, **kwargs: Any) -> T:
    try:
        return object_class.objects.get(*args, **kwargs)  # type: ignore[attr-defined]
    except (object_class.DoesNotExist, ValueError, TypeError, ValidationError):
        filters: dict[str, Any] = kwargs if kwargs else {"args": args}
        raise Http404Exception(object_name=object_class.__name__, filters=filters) from None
