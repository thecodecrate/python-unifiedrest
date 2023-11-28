from typing import Any, TypeVar

from ..declarative.remote_action import RemoteAction
from ..helpers.actions.core.action_dto.action_dto import ActionDTO

TReturnDTO = TypeVar("TReturnDTO", bound=ActionDTO)


class RemoteActionBase(RemoteAction[Any, TReturnDTO]):
    pass
