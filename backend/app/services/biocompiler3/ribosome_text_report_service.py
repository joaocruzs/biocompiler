def generate_ribosome_text_report(
    results: list[dict]
) -> str:
    """
    Gera o relatório tabular do Ribossomo.
    """

    report_lines = [
        "linha;status;resultado;proteina"
    ]

    for result in results:

        line = result.get("line", "-")

        status = result["status"]

        diagnostic = result["diagnostic"]

        protein = (
            result["protein"]
            if result.get("protein") is not None
            else "NÃO GERADA"
        )

        report_lines.append(
            f"{line};"
            f"{status};"
            f"{diagnostic};"
            f"{protein}"
        )

    return "\n".join(report_lines)