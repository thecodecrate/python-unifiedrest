from typing import Any, Generic, Optional, Type

from ..client_modules_settings.client_modules_settings_dto import (
    ClientModulesSettingsDTO,
)
from ...helpers.dto.dto import DTO
from ..helpers.classes.http_headers import HttpHeaders
from ..helpers.constants.http_verbs import HttpVerbs
from ..runner.type_returned_data import TReturnedData


class RunnerRequestDTO(DTO, Generic[TReturnedData]):
    base_url: Optional[str] = None

    url: str

    method: HttpVerbs = HttpVerbs.GET

    headers: HttpHeaders = HttpHeaders()

    body: Optional[str] = None

    files: Optional[list[Any]] = None

    return_type: Type[TReturnedData]

    client_modules_settings: Optional[ClientModulesSettingsDTO] = None
