from app.core.constants import RNA_STOP_CODONS
from app.services.biocompiler3.genetic_code import ( GENETIC_CODE )


def translate(sequence: str) -> tuple[bool, str | None, str | None]:
    """
    ARQUIVO 4 DO BIOCOMPILER 3.0
    Traduz a região codificante em trincas.

    Retorna:
    - validade
    - proteína
    - diagnóstico
    """

    protein = []

    for position in range(0, len(sequence), 3):

        codon = sequence[position:position + 3]

        if len(codon) != 3:
            return (
                False,
                None,
                "BUG - quadro de leitura"
            )

        if codon in RNA_STOP_CODONS:
            return (
                True,
                "-".join(protein),
                None
            )

        amino_acid = GENETIC_CODE.get(codon)

        if amino_acid is None:
            return (
                False,
                None,
                "BUG - quadro de leitura"
            )

        protein.append(amino_acid)

    return (
        False,
        None,
        "BUG - STOP ausente"
    )