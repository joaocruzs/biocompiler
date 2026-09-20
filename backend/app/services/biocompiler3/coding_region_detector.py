from app.core.constants import START_CODON


def find_start(sequence: str) -> int | None:
    """
    Localiza o primeiro códon AUG.
    """

    position = sequence.find(START_CODON)

    if position == -1:
        return None

    return position