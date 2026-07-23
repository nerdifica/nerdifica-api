from pydantic import BaseModel, Field


class CompoundInterestRequest(BaseModel):
    principal: float = Field(gt=0, description="Capital inicial")
    rate: float = Field(ge=0, description="Taxa de juros por período, em %")
    periods: int = Field(ge=0, description="Número de períodos")


class CompoundInterestResponse(BaseModel):
    result: float
    interest_earned: float