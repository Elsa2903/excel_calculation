from django.urls import path
from .views import ExcelCalculationView

urlpatterns = [
    path(
        "excel_calculating/", ExcelCalculationView.as_view(), name="excel_calculating"
    ),
]
