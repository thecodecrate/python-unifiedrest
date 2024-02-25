from pydantic import ConfigDict
from typing import Any, Optional, Type

from ..auth.auth_module_interface import AuthModuleInterface
from ..client_modules_settings.client_modules_settings_dto import (
    ClientModulesSettingsDTO,
)
from ..driver.driver_interface import DriverInterface
from ...helpers.dto.dto import DTO
from ..module.module_collection import ModuleCollection
from ..parser.parser_module_interface import ParserModuleInterface
from ..runner.runner import Runner
from ..serializer.serializer_module_interface import SerializerModuleInterface


class ClientSettingsDTO(DTO):
    # pydantic config
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # DTO attributes
    base_url: str

    driver: DriverInterface[Any]

    auth_module: Optional[AuthModuleInterface] = None

    serializer_module: Optional[SerializerModuleInterface] = None

    runner_modules: ModuleCollection = ModuleCollection([])

    parser_module: Optional[ParserModuleInterface] = None

    runner_class: Type[Runner] = Runner

    client_modules_settings_class: Type[ClientModulesSettingsDTO] = (
        ClientModulesSettingsDTO
    )
