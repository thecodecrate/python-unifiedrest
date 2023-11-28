from typing import Any, Optional, Type


def raise_error(klass: Type[Any], field_name: str, message: str) -> None:
    error_prefix = f"Invalid URL on {klass.__name__}.{field_name}"

    raise ValueError(f"{error_prefix}: {message}")


def validate_url(
    klass: Type[Any], field_name: str, value: Optional[str]
) -> Optional[str]:
    if value is None:
        return value

    if not value.startswith(("http://", "https://")):
        raise_error(klass, field_name, "must start with http:// or https://")

    return value
