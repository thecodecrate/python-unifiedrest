from typing import Self

from ..client_settings.client_settings_override_dto import ClientSettingsOverrideDTO
from ..client_settings.client_settings_dto import ClientSettingsDTO
from ..module.module_collection import ModuleCollection
from ..module.module_settings_dto import ModuleSettingsDTO
from ..runner.type_returned_data import TReturnedData
from ..runner_request.runner_request_dto import RunnerRequestDTO
from ..runner_response.runner_response_dto import RunnerResponseDTO


class Client:
    settings_dto: ClientSettingsDTO

    module_settings: ModuleSettingsDTO

    def __init__(self, settings_dto: ClientSettingsDTO):
        self.settings_dto = settings_dto

        self.module_settings = self.settings_dto.module_settings_class()

    def with_settings(self, settings: ClientSettingsOverrideDTO) -> Self:
        cloned_settings = self.settings_dto.model_copy()

        for field, value in settings.model_dump(exclude_none=True).items():
            setattr(cloned_settings, field, value)

        return Client(settings_dto=cloned_settings)

    def clone_request_with_defaults(
        self, request: RunnerRequestDTO[TReturnedData]
    ) -> RunnerRequestDTO[TReturnedData]:
        cloned_request = request.model_copy()

        cloned_request.base_url = cloned_request.base_url or self.settings_dto.base_url

        cloned_request.module_settings = (
            cloned_request.module_settings or self.module_settings
        )

        return cloned_request

    async def run(
        self, request: RunnerRequestDTO[TReturnedData]
    ) -> RunnerResponseDTO[TReturnedData]:
        request = self.clone_request_with_defaults(
            request=request,
        )

        runner = self.settings_dto.runner_class(
            driver=self.settings_dto.driver,
            modules=self.get_modules_merged(),
        )

        response = await runner.run(
            request=request,
        )

        return response

    def get_modules_merged(self) -> ModuleCollection:
        settings = self.settings_dto

        modules = ModuleCollection(
            [
                module
                for module in [
                    settings.auth_module,
                    settings.serializer_module,
                    *settings.runner_modules,
                    settings.parser_module,
                ]
                if module is not None
            ]
        )

        return modules
