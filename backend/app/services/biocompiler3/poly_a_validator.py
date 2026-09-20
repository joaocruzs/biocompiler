from app.core.constants import POLY_A_LENGTH


def validate_poly_a(
    sequence: str
) -> tuple[bool, str | None, str | None]:
    """
    Valida a cauda poli-A e separa o corpo do mRNA.

    Retorna:
    - validade
    - diagnóstico
    - sequência sem a cauda poli-A
    """

    poly_a = "A" * POLY_A_LENGTH

    if not sequence.endswith(poly_a):
        return False, "BUG - cauda poli-A", None

    body = sequence[:-POLY_A_LENGTH]

    if not body:
        return False, "BUG - cauda poli-A", None

    return True, None, body