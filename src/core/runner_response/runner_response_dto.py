from typing import Generic, Optional

from ...helpers.dto.dto import DTO
from ..runner.type_returned_data import TReturnedData


class RunnerResponseDTO(DTO, Generic[TReturnedData]):
    data: TReturnedData

    http_code: int

    is_success: bool

    error_message: Optional[str]

    headers: dict[str, str]
