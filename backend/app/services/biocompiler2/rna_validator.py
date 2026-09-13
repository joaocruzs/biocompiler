from app.core.constants import RNA_BASES


def validate_rna(sequence: str) -> tuple[bool, str | None]:
    """
    Valida uma sequência de pré-mRNA.

    Retorna:
        (True, None) quando a sequência é válida.
        (False, mensagem) quando a sequência é inválida.
    """

    if not sequence:
        return False, "sequência vazia"

    sequence = sequence.upper()

    invalid_bases = set(sequence) - set(RNA_BASES)

    if invalid_bases:
        return False, "base inválida"

    return True, None