from django.urls import path
from .views import ExcelCalculationView, ExcelCalculationViewCheckCells

urlpatterns = [
    path(
        "excel-calculating/", ExcelCalculationView.as_view(), name="excel-calculating"
    ),
    path(
        "excel-calculating-checking-cells/",
        ExcelCalculationViewCheckCells.as_view(),
        name="excel-calculating",
    ),
]
