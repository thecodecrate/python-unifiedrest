from typing import Generic, TypeVar

from ...helpers.actions import ActionDTO

TParamsDTO = TypeVar("TParamsDTO", bound=ActionDTO)

TInputDTO = TypeVar("TInputDTO", bound=ActionDTO)

TOutputData = TypeVar("TOutputData")


class ParamsMakeReturnFromOutput(
    ActionDTO, Generic[TParamsDTO, TInputDTO, TOutputData]
):
    params_dto: TParamsDTO
    input_dto: TInputDTO
    response_data: TOutputData
