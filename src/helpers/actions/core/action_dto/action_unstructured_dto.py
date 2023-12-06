from typing import Generic, TypeVar

from .action_dto import ActionDTO

T = TypeVar("T")


class ActionUnstructuredDTO(ActionDTO, Generic[T]):
    value: T
