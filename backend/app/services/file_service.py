def read_sequences_from_file(content: str) -> list[str]:
    """
    Lê o conteúdo de um arquivo TXT e retorna
    uma lista de sequências, uma por linha.
    """

    lines = content.splitlines()

    sequences = []

    for line in lines:
        sequence = line.strip()

        if sequence:
            sequences.append(sequence)

    return sequences