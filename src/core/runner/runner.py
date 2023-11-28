from types import NoneType
from typing import Any, Type

from ..driver.driver_interface import DriverInterface
from .exceptions.runner_http_error import RunnerHttpError
from ..module.module_collection import ModuleCollection
from ..runner_request.runner_request_dto import RunnerRequestDTO
from ..runner_response.runner_response_dto import RunnerResponseDTO
from .type_returned_data import TReturnedData


class Runner:
    driver: DriverInterface[Any]

    modules: ModuleCollection

    def __init__(
        self,
        driver: DriverInterface[Any],
        modules: ModuleCollection,
    ):
        self.driver = driver

        self.modules = modules

    async def run(
        self, request: RunnerRequestDTO[TReturnedData]
    ) -> RunnerResponseDTO[TReturnedData]:
        self.modules.before_run(request=request)

        response = await self.driver.run(request=request)

        self.modules.after_run(request=request, response=response)

        if not response.is_success:
            raise RunnerHttpError(
                http_code=response.http_code,
                message=response.error_message,
            )

        response.data = self.cast_returned_data(
            data=response.data,
            return_type=request.return_type,
        )

        return response

    def cast_returned_data(
        self, data: Any, return_type: Type[TReturnedData]
    ) -> TReturnedData:
        if (return_type is Any) or (return_type is NoneType):
            return data

        if isinstance(data, dict):
            return return_type(**data)

        return return_type(data)
