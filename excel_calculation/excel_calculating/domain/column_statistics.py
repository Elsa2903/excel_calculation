from typing import TypedDict, NamedTuple
from attrs import define

from enum import StrEnum, auto


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


class ColumnDataType(StrEnum):
    MIX = auto()
    ONE_TYPE = auto()


class CalculationResponse(NamedTuple):
    sum: float
    avg: float
