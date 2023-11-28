from typing import TypeVar

from ..action.action_interface import ActionInterface
from ..action_dto.action_dto import ActionDTO

TParamsDTO = TypeVar("TParamsDTO", bound=ActionDTO)

TReturnDTO = TypeVar("TReturnDTO", bound=ActionDTO)


class Action(ActionInterface[TParamsDTO, TReturnDTO]):
    async def run(self, params: TParamsDTO) -> TReturnDTO:
        return self.return_class(*params)
