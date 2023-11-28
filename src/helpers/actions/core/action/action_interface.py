from abc import abstractmethod
from typing import Generic, Type, TypeVar
from pydantic import BaseModel, ConfigDict

from ..action_dto.action_dto import ActionDTO

TParamsDTO = TypeVar("TParamsDTO", bound=ActionDTO)

TReturnDTO = TypeVar("TReturnDTO", bound=ActionDTO)


class ActionInterface(BaseModel, Generic[TParamsDTO, TReturnDTO]):
    # pydantic config
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # DTO attributes
    params_class: Type[TParamsDTO]

    return_class: Type[TReturnDTO]

    @abstractmethod
    async def run(self, params: TParamsDTO) -> TReturnDTO:
        pass
