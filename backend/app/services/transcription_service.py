def transcribe_dna_to_mrna(sequence: str) -> str:
    """
    Transcreve DNA para pré-mRNA,
    substituindo T por U.
    """

    return sequence.replace("T", "U")