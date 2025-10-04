from __future__ import annotations

from typing import Any

from rest_framework.exceptions import (
    AuthenticationFailed,
    MethodNotAllowed,
    NotAcceptable,
    NotAuthenticated,
    NotFound,
    PermissionDenied,
    Throttled,
    ValidationError,
)
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc: Exception, context: dict[str, Any]) -> Response | None:
    response = exception_handler(exc, context)
    if response is None:
        return None

    messages: dict[type[Exception], str] = {
        AuthenticationFailed: "Incorrect authentication credentials.",
        NotAuthenticated: "Authentication credentials were not provided.",
        MethodNotAllowed: "Method not allowed.",
        PermissionDenied: "You do not have permissions to perform this action.",
        NotFound: "Not found.",
        Throttled: "Request was throttled.",
        NotAcceptable: "Not acceptable.",
    }

    if isinstance(exc, ValidationError):
        detail = exc.detail
        message: str
        if isinstance(detail, dict):
            first_key = next(iter(detail))
            value = detail[first_key]
            if isinstance(value, list) and value:
                message = str(value[0])
            else:
                message = str(value)
        elif isinstance(detail, list) and detail:
            message = str(detail[0])
        else:
            message = str(detail)
        response.data = {
            "success": False,
            "message": message,
        }
    elif type(exc) in messages:
        response.data = {
            "success": False,
            "message": messages[type(exc)],
        }

    return response
