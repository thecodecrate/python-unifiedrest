from typing import Any, Optional

from ..core.auth.auth_module_interface import AuthModuleInterface
from ..core.client.client import Client
from ..core.client_modules_settings.client_modules_settings_dto import (
    ClientModulesSettingsDTO,
)
from ..core.client_settings.client_settings_dto import ClientSettingsDTO
from ..core.driver.driver_interface import DriverInterface
from ..core.module.module_collection import ModuleCollection
from ..core.parser.parser_module_interface import ParserModuleInterface
from ..core.runner.runner import Runner
from ..core.serializer.serializer_module_interface import SerializerModuleInterface


# syntax sugar: Client + ClientSettings in one class
class ClientDeclarative(Client):
    base_url: str

    driver: DriverInterface[Any]

    auth_module: Optional[AuthModuleInterface] = None

    serializer_module: Optional[SerializerModuleInterface] = None

    runner_modules: ModuleCollection = ModuleCollection([])

    parser_module: Optional[ParserModuleInterface] = None

    runner_class: type[Runner] = Runner

    client_modules_settings_class: type[ClientModulesSettingsDTO] = (
        ClientModulesSettingsDTO
    )

    def __init__(self, **data: Any):
        self.settings_dto = self.make_client_settings()

        super().__init__(settings_dto=self.settings_dto, **data)

    def make_client_settings(self) -> ClientSettingsDTO:
        return ClientSettingsDTO(
            base_url=self.base_url,
            driver=self.driver,
            auth_module=self.auth_module,
            serializer_module=self.serializer_module,
            runner_modules=self.runner_modules,
            parser_module=self.parser_module,
            runner_class=self.runner_class,
            client_modules_settings_class=self.client_modules_settings_class,
        )
