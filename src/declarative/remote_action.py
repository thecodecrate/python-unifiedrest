from typing import Any, Optional, Type, TypeVar

from src.declarative.make_return_from_output_action.make_return_from_output_action import (
    MakeReturnFromOutputAction,
)

from ..core.client.client import Client
from ..core.helpers.constants.http_verbs import HttpVerbs
from ..core.module.module_settings_dto import ModuleSettingsDTO
from ..core.runner_request.runner_request_dto import RunnerRequestDTO
from ..helpers.actions.core.action.action import Action
from ..helpers.actions.core.action_dto.action_dto import ActionDTO
from .make_return_from_output_action.params_make_return_from_output import (
    ParamsMakeReturnFromOutput,
)

TParamsDTO = TypeVar("TParamsDTO", bound=ActionDTO)

TReturnDTO = TypeVar("TReturnDTO", bound=ActionDTO)


class RemoteAction(Action[TParamsDTO, TReturnDTO]):
    url_template: str
    method: HttpVerbs
    params_class: Type[TParamsDTO]
    input_class: Optional[Type[ActionDTO]] = None
    output_class: Optional[Type[Any]] = Any
    return_class: Type[TReturnDTO]
    make_input_from_params: Optional[Type[Action[TParamsDTO, Any]]] = None
    make_return_from_output: Optional[
        Type[MakeReturnFromOutputAction[TReturnDTO]]
    ] = None
    client: Client
    with_settings: Optional[ModuleSettingsDTO] = None

    async def run(self, params: TParamsDTO) -> TReturnDTO:
        input_dto = await self._make_input_from_params(params=params)

        request = RunnerRequestDTO[Any](
            url=self.make_url(values_dto=params),
            method=self.method,
            module_settings=self.with_settings,
            return_type=self.output_class,
            body=input_dto.model_dump_json(),
        )

        response = await self.client.run(request=request)

        return await self._make_return_from_output(
            ParamsMakeReturnFromOutput(
                params_dto=params,
                input_dto=input_dto,
                response_data=response.data,
            )
        )

    async def _make_input_from_params(self, params: TParamsDTO) -> ActionDTO:
        if self.make_input_from_params is None:
            if self.input_class is None:
                return params

            data = params.model_dump()

            return self.input_class(**data)

        action = self.make_input_from_params(
            params_class=self.params_class,
            return_class=ActionDTO,
        )

        return await action.run(params=params)

    async def _make_return_from_output(
        self,
        payload: ParamsMakeReturnFromOutput[TParamsDTO, Any, Any],
    ) -> TReturnDTO:
        if self.make_return_from_output is not None:
            action = self.make_return_from_output(
                params_class=self.output_class,
                return_class=self.return_class,
            )

            return await action.run(params=payload)

        output_data = payload.response_data

        if isinstance(output_data, ActionDTO):
            return self.return_class(**output_data.model_dump())

        return self.return_class()

    def make_url(self, values_dto: ActionDTO) -> str:
        return self.url_template.format(**values_dto.model_dump())
