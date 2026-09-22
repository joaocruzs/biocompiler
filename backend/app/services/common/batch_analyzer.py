from app.services.biocompiler1.sequence_analyzer import analyze_sequence

def analyze_sequences(sequences: list[str]) -> list[dict]:
    """
    Analisa várias sequências de DNA.
    """
    results = []

    for index, sequence in enumerate(sequences, start=1):

        result = analyze_sequence(sequence)

        result["line"] = index

        results.append(result)

    return results