from app.core.constants import RNA_BASES

"""
ARQUIVO 1 DO BIOCOMPILER 2.0
Valida uma sequência de pré-mRNA.

Retorna:
    (True, None) quando a sequência é válida.
    (False, mensagem) quando a sequência é inválida.
"""

def validate_rna(sequence: str) -> tuple[bool, str | None]:

    if not sequence:
        return False, "sequência vazia"

    sequence = sequence.upper()

    invalid_bases = set(sequence) - set(RNA_BASES)

    if invalid_bases:
        return False, "base inválida"

    return True, None