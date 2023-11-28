from typing import Any, TypeVar

from ..core.action_dto.action_dto import ActionDTO
from ..core.action_dto.action_params_dto import ActionParamsDTO
from ..core.action_dto.action_return_dto import ActionReturnDTO
from ..core.chain_action.chain_action import ChainAction

TReturnDTO = TypeVar("TReturnDTO", bound=ActionDTO)


class ChainActionBase(ChainAction[Any, TReturnDTO]):
    params_class: Any = ActionParamsDTO

    return_class: Any = ActionReturnDTO
