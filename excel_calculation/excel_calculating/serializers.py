from typing import Any

from rest_framework import serializers


class FlexibleListField(serializers.ListField):
    def to_internal_value(self, data: Any) -> list[Any]:
        if isinstance(data, str):
            data = [x.strip() for x in data.split(",") if x.strip()]
        elif (
            isinstance(data, list)
            and len(data) == 1
            and isinstance(data[0], str)
            and "," in data[0]
        ):
            data = [x.strip() for x in data[0].split(",") if x.strip()]
        return super().to_internal_value(data)

# mypy: disable-error-code="type-arg"
class CalculactingExcelStatsIn(serializers.Serializer):
    file = serializers.FileField()
    columns = FlexibleListField(child=serializers.CharField(), allow_empty=False)


class ColumnDataOut(serializers.Serializer):
    column = serializers.CharField()
    sheet_column = serializers.CharField()
    sum = serializers.FloatField()
    average = serializers.FloatField()


class CalculactingExcelStatsOut(serializers.Serializer):
    file = serializers.CharField()
    summary = serializers.ListField(child=ColumnDataOut())
