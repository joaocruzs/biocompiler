from enum import Enum

MAX_FILE_SIZE = 1 * 1024 * 1024

VALID_BASES = {"A", "T", "C", "G"}

START_CODON = "ATG"

STOP_CODONS = {
    "TAA",
    "TAG",
    "TGA"
}


class AnalysisStatus(str, Enum):
    CORRECT = "CORRETO"
    INVALID_BASE = "BUG - base inválida"
    START_MISSING = "BUG - START ausente"
    STOP_MISSING = "BUG - STOP ausente"
    FRAMESHIFT = "BUG - frameshift"
    NONSENSE = "BUG - nonsense / STOP prematuro"