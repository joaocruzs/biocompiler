"""
ARQUIVO PRINCIPAL DO BIOCOMPILER 1.0
Cria um resultado padronizado para todas as análises.
"""

from app.core.constants import (
    AnalysisStatus,
    START_CODON,
    RNA_STOP_CODONS,
)

from app.services.biocompiler1.dna_validator import validate_sequence
from app.services.biocompiler1.transcription_service import transcribe_dna_to_mrna

def build_result(
    sequence: str,
    status: AnalysisStatus,
    start_position=None,
    stop_position=None,
    stop_codon=None,
    mrna=None
):

    return {
        "sequence": sequence,
        "status": status,
        "start_position": start_position,
        "stop_position": stop_position,
        "stop_codon": stop_codon,
        "mrna": mrna
    }


def analyze_sequence(sequence: str) -> dict:

    sequence = sequence.strip().upper()

    # Caso 2 — Base inválida
    if not validate_sequence(sequence):
        return build_result(
            sequence,
            AnalysisStatus.INVALID_BASE
        )

    # Caso 3 — START ausente
    start_index = sequence.find(START_CODON)

    if start_index == -1:
        return build_result(
            sequence,
            AnalysisStatus.START_MISSING
        )

    # Sequência a partir do START
    coding_sequence = sequence[start_index:]

    # Caso 5 — Frameshift
    if len(coding_sequence) % 3 != 0:
        return build_result(
            sequence,
            AnalysisStatus.FRAMESHIFT,
            start_position=start_index
        )

    # Procurar STOP no quadro de leitura
    stop_position = None
    stop_codon = None

    for i in range(3, len(coding_sequence), 3):

        codon = coding_sequence[i:i + 3]

        if codon in RNA_STOP_CODONS:
            stop_position = start_index + i
            stop_codon = codon
            break

    # Caso 4 — STOP ausente
    if stop_position is None:
        return build_result(
            sequence,
            AnalysisStatus.STOP_MISSING,
            start_position=start_index
        )

    # Caso 6 — STOP prematuro
    end_of_stop = stop_position + 3

    if end_of_stop < len(sequence):
        return build_result(
            sequence,
            AnalysisStatus.NONSENSE,
            start_position=start_index,
            stop_position=stop_position,
            stop_codon=stop_codon
        )

    # Caso 1 — Correto
    mrna = transcribe_dna_to_mrna(sequence)

    return build_result(
        sequence,
        AnalysisStatus.CORRECT,
        start_position=start_index,
        stop_position=stop_position,
        stop_codon=stop_codon,
        mrna=mrna
    )