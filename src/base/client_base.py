from typing import Any

from ..addons.drivers.simple_driver.simple_driver import SimpleDriver
from ..addons.parsers.json.parser_json_module import ParserJsonModule
from ..addons.serializers.json.serializer_json_module import SerializerJsonModule
from ..base.client_modules_settings_base import ClientModulesSettingsBase
from ..core.driver.driver_interface import DriverInterface
from ..declarative.client import ClientDeclarative


class ClientBase(ClientDeclarative):
    driver: DriverInterface[Any] = SimpleDriver()

    client_modules_settings_class: Any = ClientModulesSettingsBase

    serializer_module: Any = SerializerJsonModule()

    parser_module: Any = ParserJsonModule()
