from collections import Counter


def generate_summary(results: list[dict]) -> dict:
    """
    Gera estatísticas gerais da análise.
    """

    status_counter = Counter(
        result["status"]
        for result in results
    )

    return {
        "total_sequences": len(results),
        "correct": status_counter.get("CORRETO", 0),
        "invalid_base": status_counter.get(
            "BUG - base inválida", 0
        ),
        "start_missing": status_counter.get(
            "BUG - START ausente", 0
        ),
        "stop_missing": status_counter.get(
            "BUG - STOP ausente", 0
        ),
        "frameshift": status_counter.get(
            "BUG - frameshift", 0
        ),
        "nonsense": status_counter.get(
            "BUG - nonsense / STOP prematuro", 0
        )
    }