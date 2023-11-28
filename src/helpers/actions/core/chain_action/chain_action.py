from typing import TypeVar

from ..action.action_interface import ActionInterface
from ..action_dto.action_dto import ActionDTO
from ..chain_action.type_actions_classes import ActionsClasses

TParamsDTO = TypeVar("TParamsDTO", bound=ActionDTO)

TReturnDTO = TypeVar("TReturnDTO", bound=ActionDTO)


class ChainAction(ActionInterface[TParamsDTO, TReturnDTO]):
    actions: ActionsClasses = []

    async def run(self, params: TParamsDTO) -> TReturnDTO:
        payload = params

        for action_class in self.actions:
            action = action_class(
                params_class=ActionDTO,
                return_class=ActionDTO,
            )

            payload = await action.run(params=payload)

        return self.return_class(*payload)
