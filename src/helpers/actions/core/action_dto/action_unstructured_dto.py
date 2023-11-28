from typing import Generic, TypeVar

from src.helpers.actions.core.action_dto.action_dto import ActionDTO

T = TypeVar("T")


class ActionUnstructuredDTO(ActionDTO, Generic[T]):
    value: T
