class NerdificaException(Exception):
    """Base exception for all domain-level errors."""

    status_code = 400
    detail = "Something went wrong"

    def __init__(self, detail: str | None = None) -> None:
        if detail:
            self.detail = detail
        super().__init__(self.detail)