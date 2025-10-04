from rest_framework.exceptions import (
    AuthenticationFailed,
    NotAuthenticated,
    MethodNotAllowed,
    ValidationError,
    PermissionDenied,
    NotFound,
    Throttled,
    NotAcceptable,
)
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        messages = {
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
            if isinstance(detail, dict):
                first_key = next(iter(detail))
                first_msg = (
                    detail[first_key][0]
                    if isinstance(detail[first_key], list)
                    else detail[first_key]
                )
                message = first_msg
            elif isinstance(detail, list):
                message = detail[0]
            else:
                message = str(detail)
            response.data = {
                "success": False,
                "message": message,
            }
        elif type(exc) in messages:
            response.data = {
                "success": False,
                "message": messages.get(type(exc)),
            }
    return response
