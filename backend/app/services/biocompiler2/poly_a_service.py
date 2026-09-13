from app.core.constants import POLY_A_LENGTH


def add_poly_a(sequence: str) -> str:
    """
    Adiciona exatamente 100 adeninas
    à extremidade 3' do RNA.
    """

    return sequence + ("A" * POLY_A_LENGTH)