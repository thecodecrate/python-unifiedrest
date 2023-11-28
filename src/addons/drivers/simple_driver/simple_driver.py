import requests
from typing import Any

from ....core.driver.driver_interface import DriverInterface
from ....core.helpers.combine_urls_safely import combine_urls_safely
from ....core.runner_request.runner_request_dto import RunnerRequestDTO
from ....core.runner_response.runner_response_dto import RunnerResponseDTO


class SimpleDriver(DriverInterface[requests.Response]):
    async def run(self, request: RunnerRequestDTO[Any]) -> RunnerResponseDTO[Any]:
        url = combine_urls_safely(request.base_url, request.url)

        driver_response = requests.request(
            url=url,
            method=request.method.value,
            headers=request.headers,
            data=request.body,
        )

        http_code = driver_response.status_code

        return RunnerResponseDTO(
            data=driver_response.text,
            http_code=http_code,
            is_success=http_code >= 200 and http_code < 300,
            error_message=driver_response.reason,
            headers=dict[str, str](driver_response.headers),
        )
