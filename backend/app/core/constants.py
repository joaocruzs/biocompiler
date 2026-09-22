from enum import Enum

# Constantes do Biocompiler 1.0
MAX_FILE_SIZE = 1 * 1024 * 1024

VALID_BASES = {"A", "T", "C", "G"}

START_CODON = "ATG"

RNA_STOP_CODONS = {
    "TAA",
    "TAG",
    "TGA"
}




# Biocompielr 1.0 Análise dos Status
class AnalysisStatus(str, Enum):
    CORRECT = "CORRETO"
    INVALID_BASE = "BUG - base inválida"
    START_MISSING = "BUG - START ausente"
    STOP_MISSING = "BUG - STOP ausente"
    FRAMESHIFT = "BUG - frameshift"
    NONSENSE = "BUG - nonsense / STOP prematuro"



# Constantes do Biocompiler 2.0
RNA_BASES = {"A", "U", "C", "G"}

SPLICE_SITE_5 = "GU"
SPLICE_SITE_3 = "AG"

BRANCH_POINT_BASE = "A"

MIN_BRANCH_DISTANCE = 10
MAX_BRANCH_DISTANCE = 30

CAP_5 = "m7Gppp"
POLY_A_LENGTH = 100



# Constantes do Biocompiler 3.0
RNA_START_CODON = "AUG"

RNA_STOP_CODONS = {
    "UAA",
    "UAG",
    "UGA"
}