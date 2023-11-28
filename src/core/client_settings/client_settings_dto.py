from pydantic import ConfigDict
from typing import Any, Optional, Type

from ..auth.auth_module_interface import AuthModuleInterface
from ..driver.driver_interface import DriverInterface
from ...helpers.dto.dto import DTO
from ..module.module_collection import ModuleCollection
from ..module.module_settings_dto import ModuleSettingsDTO
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

    module_settings_class: Type[ModuleSettingsDTO] = ModuleSettingsDTO
