from fastapi import APIRouter

from src.financas.schemas import CompoundInterestRequest, CompoundInterestResponse
from src.financas.service import calculate_compound_interest

router = APIRouter(prefix="/financas", tags=["financas"])


@router.post("/juros-compostos", response_model=CompoundInterestResponse)
def compound_interest(data: CompoundInterestRequest) -> CompoundInterestResponse:
    return calculate_compound_interest(data)