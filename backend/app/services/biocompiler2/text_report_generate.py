def generate_text_report(
    results: list[dict]
) -> str:
    """
    Gera o relatório tabular do BioCompiler 2.0.

    Formato:
    linha;status;resultado;mRNA_maduro
    """

    report_lines = [
        "linha;status;resultado;mRNA_maduro"
    ]

    for result in results:

        line = result.get("line", "-")

        status = result["status"]

        diagnostic = result["diagnostic"]

        mature_mrna = (
            result["mature_mrna"]
            if result.get("mature_mrna") is not None
            else "NÃO GERADO"
        )

        report_lines.append(
            f"{line};"
            f"{status};"
            f"{diagnostic};"
            f"{mature_mrna}"
        )

    return "\n".join(report_lines)