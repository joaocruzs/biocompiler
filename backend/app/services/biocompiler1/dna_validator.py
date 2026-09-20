from app.core.constants import VALID_BASES

"""
ARQUIVO 1 DO BIOCOMPILER 1.0
Retorna as bases inválidas encontradas na sequência.
"""

def get_invalid_bases(sequence: str) -> set[str]:

    return set(sequence) - VALID_BASES

def validate_sequence(sequence: str) -> bool:

    return len(get_invalid_bases(sequence)) == 0