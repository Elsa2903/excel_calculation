from typing import Any
from rest_framework import status
from rest_framework.response import Response

from .domain.exceptions import (
    ColumnNamesNotExsistingException,
    CannotCalculateDataForThatColumnException,
)
from rest_framework.views import exception_handler

EXCEPTIONS = {
    CannotCalculateDataForThatColumnException: status.HTTP_400_BAD_REQUEST,
    ColumnNamesNotExsistingException: status.HTTP_403_FORBIDDEN,
}


def custom_exception_handler(exc: Exception, context: dict[str, Any]) -> Response:

    response = exception_handler(exc, context)

    if response is not None:
        return response
    for exc_type, code in EXCEPTIONS.items():
        if isinstance(exc, exc_type):
            return Response(
                {"detail": str(exc)},  # <--- use the exception message
                status=code,
            )

    return Response(
        {"detail": "Server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
