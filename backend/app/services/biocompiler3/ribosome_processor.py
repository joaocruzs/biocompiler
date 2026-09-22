"""
ARQUIVO PRINCIPAL DO BIOCOMPILER 3.0:

1. (cap_validator)
2. (poly_a_validator)
3. (coding_region_detector)
4. (translation_service --> genetic_code)
"""

from app.core.constants import CAP_5
from app.core.constants import RNA_BASES

from app.services.biocompiler3.cap_validator import ( validate_cap )
from app.services.biocompiler3.poly_a_validator import ( validate_poly_a )
from app.services.biocompiler3.coding_region_detector import ( find_start )
from app.services.biocompiler3.translation_service import ( translate )

def process_mature_mrna(sequence: str) -> dict:
    sequence = sequence.strip()

    cap_valid, cap_error = validate_cap(sequence)

    if not cap_valid:
        return {
            "status": "ERRO",
            "diagnostic": cap_error,
            "protein": None,
        }

    sequence_without_cap = sequence[len(CAP_5):]

    poly_a_valid, poly_a_error, body = validate_poly_a(
        sequence_without_cap
    )

    if not poly_a_valid:
        return {
            "status": "ERRO",
            "diagnostic": poly_a_error,
            "protein": None,
        }

    invalid_bases = set(body) - RNA_BASES

    if invalid_bases:
        return {
            "status": "ERRO",
            "diagnostic": "BUG - base inválida",
            "protein": None,
        }

    start_position = find_start(body)

    if start_position is None:
        return {
            "status": "ERRO",
            "diagnostic": "BUG - START ausente",
            "protein": None,
        }

    coding_region = body[start_position:]

    success, protein, error = translate(coding_region)

    if not success:
        return {
            "status": "ERRO",
            "diagnostic": error,
            "protein": None,
        }

    return {
        "status": "OK",
        "diagnostic": "CORRETO",
        "protein": protein,
    }