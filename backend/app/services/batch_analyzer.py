from app.services.sequence_analyzer import analyze_sequence


def analyze_sequences(sequences: list[str]) -> list[dict]:
    """
    Analisa múltiplas sequências de DNA.
    """

    results = []

    for index, sequence in enumerate(sequences, start=1):

        result = analyze_sequence(sequence)

        result["line"] = index

        results.append(result)

    return results