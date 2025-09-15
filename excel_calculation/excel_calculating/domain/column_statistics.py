from typing import TypedDict
from attrs import define


@define
class SheetData:
    columns_name: set[str]
    sheet_name: str
    header_row: int


class ColumnStatistics(TypedDict):
    column: str
    sheet_column: str
    sheet: str
    sum: float
    avg: float
