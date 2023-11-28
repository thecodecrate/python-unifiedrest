from typing import Any, List

from .module_interface import ModuleInterface
from ..runner.type_returned_data import TReturnedData
from ..runner_request.runner_request_dto import RunnerRequestDTO
from ..runner_response.runner_response_dto import RunnerResponseDTO


class ModuleCollection(List[ModuleInterface]):
    def before_run(self, request: RunnerRequestDTO[Any]) -> None:
        for module in self:
            module.before_run(request=request)

    def after_run(
        self,
        request: RunnerRequestDTO[TReturnedData],
        response: RunnerResponseDTO[TReturnedData],
    ) -> None:
        for module in self:
            module.after_run(request=request, response=response)
