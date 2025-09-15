from ..domain.column_statistics import SheetData
from pandas import ExcelFile, read_excel
from ..domain.exceptions import ColumnNamesNotExsistingException
from typing import cast


def find_columns_and_row_in_sheets(
    columns_names: set[str], excel_file: ExcelFile
) -> list[SheetData]:
    results: list[SheetData] = []
    used_columns: list[str] = []
    for sheet in excel_file.sheet_names:
        preview = read_excel(excel_file, sheet_name=sheet, header=None, nrows=6)
        for row_idx in range(len(preview)):
            row_values = preview.iloc[row_idx].astype(str).str.strip().str.lower()
            matches = columns_names.intersection(row_values)
            if matches:
                used_columns.extend(matches)
                results.append(
                    SheetData(
                        sheet_name=cast(str, sheet),
                        header_row=row_idx,
                        columns_name=matches,
                    )
                )
                break
    if columns_names != set(used_columns):
        raise ColumnNamesNotExsistingException(columns_names.difference(used_columns))
    return results
