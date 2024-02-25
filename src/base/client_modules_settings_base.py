from ..addons.auth.bear_token.auth_bear_token_settings import AuthBearTokenSettings
from ..addons.serializers.json.serializer_json_settings import SerializerJsonSettings
from ..core.module.module_settings_dto import ModuleSettingsDTO


class ClientModulesSettingsBase(
    AuthBearTokenSettings,
    SerializerJsonSettings,
    ModuleSettingsDTO,
):
    pass
