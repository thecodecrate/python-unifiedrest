from pydantic import ConfigDict
from typing import Any, Optional, Type

from ..auth.auth_module_interface import AuthModuleInterface
from ..driver.driver_interface import DriverInterface
from ...helpers.dto.dto import DTO
from ..module.module_collection import ModuleCollection
from ..parser.parser_module_interface import ParserModuleInterface
from ..runner.runner import Runner
from ..serializer.serializer_module_interface import SerializerModuleInterface


class ClientSettingsOverrideDTO(DTO):
    # pydantic config
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # DTO attributes
    base_url: Optional[str] = None

    driver: Optional[DriverInterface[Any]] = None

    auth_module: Optional[AuthModuleInterface] = None

    serializer_module: Optional[SerializerModuleInterface] = None

    runner_modules: Optional[ModuleCollection] = None

    parser_module: Optional[ParserModuleInterface] = None

    runner_class: Optional[Type[Runner]] = None
