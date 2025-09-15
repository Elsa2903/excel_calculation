from django.urls import path
from .views import ExcelCalculationView

urlpatterns = [
    path(
        "excel-calculating/", ExcelCalculationView.as_view(), name="excel-calculating"
    ),
]
