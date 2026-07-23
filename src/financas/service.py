from src.financas.schemas import CompoundInterestRequest, CompoundInterestResponse


def calculate_compound_interest(data: CompoundInterestRequest) -> CompoundInterestResponse:
    rate_decimal = data.rate / 100
    result = data.principal * (1 + rate_decimal) ** data.periods
    return CompoundInterestResponse(
        result=round(result, 2),
        interest_earned=round(result - data.principal, 2),
    )