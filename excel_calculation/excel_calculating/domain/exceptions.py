class ColumnNamesNotExsistingException(Exception):
    def __init__(self, names: set[str]) -> None:
        message = f"Columns with names {names} do not exist in given excel file"
        super().__init__(message)


class CannotCalculateDataForThatColumnException(Exception):
    def __init__(self, name: str) -> None:
        message = f"Cannot calculate data for column {name} with given excel file"
        super().__init__(message)

class UploadTypeInWrongTypeException(Exception):
    def __init__(self, name: str) -> None:
        message = f"Cannot open file with {name}. Wrong type"
        super().__init__(message)
