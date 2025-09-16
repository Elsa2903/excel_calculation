from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    CalculactingExcelStatsIn,
    CalculactingExcelStatsOut,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, parsers
from .application.excel_calculation_service import calculate_columns_statistics


class ExcelCalculationView(APIView):
    parser_classes = [parsers.MultiPartParser]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="file",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=True,
                description="Upload Excel file",
            ),
            openapi.Parameter(
                name="columns",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_STRING),
                required=True,
                description="Columns for calculation",
            ),
        ],
        consumes=["multipart/form-data"],
        responses={200: "Excel processed"},
    )  # type: ignore[misc]
    def post(self, request: Request) -> Response:
        serializer = CalculactingExcelStatsIn(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        uploaded_file = serializer.validated_data["file"]
        columns = serializer.validated_data["columns"]
        result = calculate_columns_statistics(
            columns_names=columns, uploaded_file=uploaded_file
        )
        if serializer.is_valid():
            return Response(
                CalculactingExcelStatsOut(
                    {
                        "file": uploaded_file.name,
                        "summary": result,
                    }
                ).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
