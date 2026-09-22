from app.core.constants import CAP_5


def validate_cap(sequence: str) -> tuple[bool, str | None]:
    """
    ARQUIVO 1 DO BIOCOMPILER 3.0
    Valida a representação didática da CAP 5'.
    """

    if not sequence.startswith(CAP_5):
        return False, "BUG - CAP 5'"

    return True, None