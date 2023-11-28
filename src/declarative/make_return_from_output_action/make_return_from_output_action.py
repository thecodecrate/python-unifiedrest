from abc import abstractmethod
from typing import Any, TypeVar

from ...helpers.actions import ActionBase, ActionDTO
from .params_make_return_from_output import ParamsMakeReturnFromOutput

TReturnDTO = TypeVar("TReturnDTO", bound=ActionDTO)


class MakeReturnFromOutputAction(ActionBase[TReturnDTO]):
    @abstractmethod
    async def run(
        self,
        params: ParamsMakeReturnFromOutput[Any, Any, Any],
    ) -> TReturnDTO:
        pass
