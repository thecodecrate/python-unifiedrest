from ....core.module.module_settings_dto import ModuleSettingsDTO


class AuthBearTokenSettings(ModuleSettingsDTO):
    disable_unauthorized_handling: bool = False
