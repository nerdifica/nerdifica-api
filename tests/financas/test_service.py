from src.financas.schemas import CompoundInterestRequest
from src.financas.service import calculate_compound_interest


def test_calculate_compound_interest() -> None:
    result = calculate_compound_interest(
        CompoundInterestRequest(principal=1000, rate=1, periods=12)
    )

    assert result.result == 1126.83
    assert result.interest_earned == 126.83