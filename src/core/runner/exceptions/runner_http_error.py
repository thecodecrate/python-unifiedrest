from typing import Optional

from .runner_error_interface import RunnerErrorInterface


class RunnerHttpError(RunnerErrorInterface):
    http_code: int

    def __init__(
        self,
        http_code: int,
        message: Optional[str] = None,
    ):
        self.http_code = http_code

        self.message = message or f"The REST API returned an error code {http_code}"

        super().__init__(self.message)
