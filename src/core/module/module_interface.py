from abc import ABC, abstractmethod
from typing import Any

from ..runner.type_returned_data import TReturnedData
from ..runner_request.runner_request_dto import RunnerRequestDTO
from ..runner_response.runner_response_dto import RunnerResponseDTO


class ModuleInterface(ABC):
    @abstractmethod
    def before_run(self, request: RunnerRequestDTO[Any]) -> None:
        pass

    @abstractmethod
    def after_run(
        self,
        request: RunnerRequestDTO[TReturnedData],
        response: RunnerResponseDTO[TReturnedData],
    ) -> None:
        pass
