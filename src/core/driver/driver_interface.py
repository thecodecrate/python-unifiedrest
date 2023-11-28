from abc import ABC, abstractmethod
from typing import Generic

from ..runner_request.runner_request_dto import RunnerRequestDTO
from ..runner_response.runner_response_dto import RunnerResponseDTO
from ..runner.type_returned_data import TReturnedData
from .type_driver_response import TDriverResponse


class DriverInterface(ABC, Generic[TDriverResponse]):
    @abstractmethod
    async def run(
        self, request: RunnerRequestDTO[TReturnedData]
    ) -> RunnerResponseDTO[TReturnedData]:
        pass
