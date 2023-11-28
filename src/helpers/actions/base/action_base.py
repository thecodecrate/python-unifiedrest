from typing import Any, TypeVar

from ..core.action.action import Action
from ..core.action_dto.action_dto import ActionDTO
from ..core.action_dto.action_params_dto import ActionParamsDTO
from ..core.action_dto.action_return_dto import ActionReturnDTO

TReturnDTO = TypeVar("TReturnDTO", bound=ActionDTO)


class ActionBase(Action[Any, TReturnDTO]):
    params_class: Any = ActionParamsDTO

    return_class: Any = ActionReturnDTO
