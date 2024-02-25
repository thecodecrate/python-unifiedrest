from typing import Any, Optional, cast

from ....addons.auth.bear_token.auth_bear_token_settings import AuthBearTokenSettings
from ....core.auth.auth_module_interface import AuthModuleInterface
from ....core.helpers.classes.http_headers import HttpHeaders
from ....core.runner.type_returned_data import TReturnedData
from ....core.runner_request.runner_request_dto import RunnerRequestDTO
from ....core.runner_response.runner_response_dto import RunnerResponseDTO

HTTP_UNAUTHORIZED = 403


class AuthBearTokenModule(AuthModuleInterface):
    def add_auth_headers(self, headers: HttpHeaders) -> None:
        token = self.load_stored_auth_token()

        if token:
            headers.add_headers({"Authorization": f"Bearer {token}"})

    def before_run(self, request: RunnerRequestDTO[Any]) -> None:
        self.add_auth_headers(request.headers)

    def after_run(
        self,
        request: RunnerRequestDTO[TReturnedData],
        response: RunnerResponseDTO[TReturnedData],
    ) -> None:
        settings_dto = cast(AuthBearTokenSettings, request.client_modules_settings)

        with_unauthorized_handling = not settings_dto.disable_unauthorized_handling

        if response.http_code == HTTP_UNAUTHORIZED and with_unauthorized_handling:
            self.handle_unauthorized()

    def load_stored_auth_token(self) -> Optional[str]:
        pass

    def delete_stored_auth_token(self) -> None:
        pass

    def delete_stored_auth_user(self) -> None:
        pass

    def handle_unauthorized(self) -> None:
        self.delete_stored_auth_token()

        self.delete_stored_auth_user()
