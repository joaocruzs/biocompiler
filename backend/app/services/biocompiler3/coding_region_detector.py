from app.core.constants import RNA_START_CODON


def find_start(sequence: str) -> int | None:
    """
    ARQUIVO 3 DO BIOCOMPILER 3.0
    Localiza o primeiro códon AUG.
    """

    position = sequence.find(RNA_START_CODON)

    if position == -1:
        return None

    return position