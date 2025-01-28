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
            ValidationError: "Invalid input.",
            PermissionDenied: "You do not have permissions to perform this action.",
            NotFound: "Not found.",
            Throttled: "Request was throttled.",
            NotAcceptable: "Not acceptable.",
        }
        if type(exc) in messages:
            response.data = {
                "success": False,
                "message": messages.get(type(exc)),
            }
    return response
