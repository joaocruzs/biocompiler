def generate_text_report(
    results: list[dict],
    summary: dict
) -> str:
    """
    Gera um relatório em formato TXT
    com os resultados da análise.
    """

    report = []

    report.append("=" * 50)
    report.append("BIOCOMPILER - RELATÓRIO DE ANÁLISE")
    report.append("=" * 50)

    report.append("")
    report.append(
        f"Total de sequências: "
        f"{summary['total_sequences']}"
    )

    report.append("")
    report.append("RESUMO")
    report.append("-" * 50)

    report.append(
        f"CORRETO: {summary['correct']}"
    )

    report.append(
        f"BUG - base inválida: "
        f"{summary['invalid_base']}"
    )

    report.append(
        f"BUG - START ausente: "
        f"{summary['start_missing']}"
    )

    report.append(
        f"BUG - STOP ausente: "
        f"{summary['stop_missing']}"
    )

    report.append(
        f"BUG - frameshift: "
        f"{summary['frameshift']}"
    )

    report.append(
        f"BUG - nonsense / STOP prematuro: "
        f"{summary['nonsense']}"
    )

    report.append("")
    report.append("=" * 50)
    report.append("DETALHAMENTO")
    report.append("=" * 50)

    for result in results:

        report.append("")
        report.append(
            f"Linha {result.get('line', '-')}"
        )

        report.append(
            f"DNA: {result['sequence']}"
        )

        report.append(
            f"Status: {result['status']}"
        )

        if result.get("start_position") is not None:
            report.append(
                f"Posição START: "
                f"{result['start_position']}"
            )

        if result.get("stop_position") is not None:
            report.append(
                f"Posição STOP: "
                f"{result['stop_position']}"
            )

        if result.get("stop_codon"):
            report.append(
                f"Códon STOP: "
                f"{result['stop_codon']}"
            )

        if result.get("mrna"):
            report.append(
                f"pré-mRNA: "
                f"{result['mrna']}"
            )

        report.append("-" * 50)

    return "\n".join(report)