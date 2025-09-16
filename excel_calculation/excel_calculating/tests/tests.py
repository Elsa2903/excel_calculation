import io
from pathlib import Path
from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase


class ExcelCalculationTests(APITestCase):
    test_file_path = Path(
        settings.BASE_DIR, "excel_calculating/tests/static/test_data.xlsx"
    )

    def load_temp_excel_file(self) -> io.BufferedReader:
        return open(self.test_file_path, "rb")

    def test_upload_excel_and_columns(self) -> None:
        file = self.load_temp_excel_file()
        data = {"file": file, "columns": ["current usd"]}

        response = self.client.post(
            "/excel_calculating/excel-calculating/", data, format="multipart"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["summary"][0],
            {
                "column": "current usd",
                "sheet_column": "E",
                "sheet": "Complete Range",
                "sum": 36639.38,
                "avg": 54.44,
            },
        )
        self.assertEqual(response.data["file"], "test_data.xlsx")

    def test_upload_excel_and_columns_fails_on_wrong_column_name(self) -> None:
        file = self.load_temp_excel_file()
        data = {"file": file, "columns": ["tests"]}

        response = self.client.post(
            "/excel_calculating/excel-calculating/", data, format="multipart"
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(
            response.data["detail"],
            "Columns with names {'tests'} do not exist in given excel file",
        )

    def test_upload_excel_and_columns_fails_on_wrong_column_data(self) -> None:
        file = self.load_temp_excel_file()
        data = {"file": file, "columns": ["Description"]}
        response = self.client.post(
            "/excel_calculating/excel-calculating/", data, format="multipart"
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(
            response.data["detail"],
            "Cannot calculate data for column description with given excel file",
        )
