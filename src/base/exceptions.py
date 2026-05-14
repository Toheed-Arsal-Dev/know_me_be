from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """
    Custom exception handler to format error responses consistently.

    Error response format:
    {
        "success": false,
        "message": "ValidationError: Invalid input.",
        "data": null,
        "errors": {
            "name": [
                "This field is required."
            ],
            "config": [
                "This field is required."
            ]
        }
    }
    """
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, ValidationError):
            message = f"{exc.__class__.__name__}: {exc.default_detail}"
            errors = response.data
        else:
            message = str(response.data.get("detail", str(exc)))
            errors = {"reason": message}

        response.data = {
            "success": False,
            "message": message,
            "data": None,
            "errors": errors,
        }

    return response
