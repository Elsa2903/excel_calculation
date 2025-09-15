from pandas import ExcelFile, read_excel
from ..domain.column_statistics import ColumnStatistics
from .excel_loader_service import find_columns_and_row_in_sheets
from openpyxl.utils import get_column_letter
from ..domain.exceptions import CannotCalculateDataForThatColumnException
from typing import cast


def calculate_columns_statistics(
    columns_names: list[str], excel_file: ExcelFile
) -> list[ColumnStatistics]:
    sheets = find_columns_and_row_in_sheets(
        columns_names={col.strip().lower() for col in columns_names},
        excel_file=ExcelFile(excel_file),
    )
    result = []
    for i in sheets:
        df = read_excel(excel_file, sheet_name=i.sheet_name, header=i.header_row)
        #      df = df.dropna(axis=1, how="all")  # drop all empty columns
        #      df = df.dropna(axis=0, how="all")  # drop all empty raws
        #  df1 = df1.dropna(axis=0, thresh=6)
        df.columns = df.columns.str.strip().str.lower()
        col_names = {
            col
            for col in df.columns
            for col_name in i.columns_name
            if col.lower().startswith(col_name)
        }
        for col in col_names:
            column_index: int = cast(int, df.columns.get_loc(col))
            try:
                result.append(
                    ColumnStatistics(
                        sheet_column=get_column_letter(column_index + 1),
                        column=col,
                        sheet=i.sheet_name,
                        sum=round(df[col].sum(), 2),
                        avg=round(df[col].mean(), 2),
                    )
                )
            except TypeError as err:
                raise CannotCalculateDataForThatColumnException(col) from err

    return result
