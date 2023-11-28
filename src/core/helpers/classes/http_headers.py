from typing import Any, Dict, Self


class HttpHeaders(Dict[str, str]):
    def add_headers(self, entries: Dict[str, str]) -> Self:
        for key, value in entries.items():
            self[key] = value

        return self

    # Required for Pydantic
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    # Required for Pydantic
    @classmethod
    def validate(cls, value: Any):
        if not isinstance(value, dict):
            raise TypeError("Input value must be a dictionary")
        return cls(value)  # type: ignore
