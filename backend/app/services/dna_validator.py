from app.core.constants import VALID_BASES


def get_invalid_bases(sequence: str) -> set[str]:
    """
    Retorna as bases inválidas encontradas na sequência.
    """

    return set(sequence) - VALID_BASES


def validate_sequence(sequence: str) -> bool:
    """
    Verifica se a sequência contém apenas
    A, T, C e G.
    """

    return len(get_invalid_bases(sequence)) == 0