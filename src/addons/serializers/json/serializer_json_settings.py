from pydantic import BaseModel
from typing import Optional

from ....core.module.module_settings_dto import ModuleSettingsDTO


class SerializerJsonSettings(ModuleSettingsDTO):
    disable_json_headers: bool = False

    body_object: Optional[BaseModel] = None
