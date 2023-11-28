import json
from typing import Any

from ....core.parser.parser_module_interface import ParserModuleInterface
from ....core.runner.type_returned_data import TReturnedData
from ....core.runner_request.runner_request_dto import RunnerRequestDTO
from ....core.runner_response.runner_response_dto import RunnerResponseDTO


class ParserJsonModule(ParserModuleInterface):
    def before_run(self, request: RunnerRequestDTO[Any]) -> None:
        pass

    def after_run(
        self,
        request: RunnerRequestDTO[TReturnedData],
        response: RunnerResponseDTO[TReturnedData],
    ) -> None:
        if not isinstance(response.data, str):
            return

        try:
            json_decoded = json.loads(response.data)

            response.data = json_decoded
        except:
            pass
