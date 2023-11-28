import json
from typing import Any, cast

from ....core.helpers.classes.http_headers import HttpHeaders
from ....core.runner.type_returned_data import TReturnedData
from ....core.runner_request.runner_request_dto import RunnerRequestDTO
from ....core.runner_response.runner_response_dto import RunnerResponseDTO
from ....core.serializer.serializer_module_interface import SerializerModuleInterface
from .serializer_json_settings import SerializerJsonSettings


class SerializerJsonModule(SerializerModuleInterface):
    def may_add_json_headers(
        self, settings_dto: SerializerJsonSettings, headers: HttpHeaders
    ) -> None:
        if settings_dto.disable_json_headers:
            return

        headers.add_headers(
            {
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    def may_add_json_body(
        self,
        settings_dto: SerializerJsonSettings,
        request: RunnerRequestDTO[Any],
    ) -> None:
        body_object = settings_dto.body_object

        if body_object == None:
            return

        request.body = json.dumps(body_object)

    def before_run(self, request: RunnerRequestDTO[Any]) -> None:
        settings_dto = cast(SerializerJsonSettings, request.module_settings)

        self.may_add_json_headers(settings_dto=settings_dto, headers=request.headers)

        self.may_add_json_body(settings_dto=settings_dto, request=request)

    def after_run(
        self,
        request: RunnerRequestDTO[TReturnedData],
        response: RunnerResponseDTO[TReturnedData],
    ) -> None:
        pass
