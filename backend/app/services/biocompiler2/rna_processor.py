from app.services.biocompiler2.rna_validator import validate_rna
from app.services.biocompiler2.intron_validator import validate_intron
from app.services.biocompiler2.splicing_service import splice
from app.services.biocompiler2.capping_service import add_cap
from app.services.biocompiler2.poly_a_service import add_poly_a

"""
ARQUIVO PRINCIPAL DO BIOCOMPILER 2.0
Processa um pré-mRNA completo:

1. Validação (rna_validator)
2. Identificação dos sinais de splicing
    (intron_validator --> splice_site_detector)
3. Splicing (splicing_service)
4. CAP 5' (capping_service)
5. Cauda poli-A (poly_a_service)
"""

def process_pre_mrna(sequence: str) -> dict:

    sequence = sequence.strip().upper()

    # --------------------------------------------------
    # 1. VALIDAÇÃO DO RNA
    # --------------------------------------------------

    valid, error = validate_rna(sequence)

    if not valid:
        return {
            "status": "ERRO",
            "diagnostic": f"BUG - {error}",
            "five_prime_site": None,
            "branch_point": None,
            "three_prime_site": None,
            "spliced_rna": None,
            "mature_mrna": None,
        }

    # --------------------------------------------------
    # 2. VALIDAÇÃO DO INTRON
    # --------------------------------------------------

    intron_result = validate_intron(sequence)

    if intron_result["status"] != "OK":
        return {
            "status": intron_result["status"],
            "diagnostic": intron_result["diagnostic"],
            "five_prime_site": intron_result["five_prime_site"],
            "branch_point": intron_result["branch_point"],
            "three_prime_site": intron_result["three_prime_site"],
            "spliced_rna": None,
            "mature_mrna": None,
        }

    five_prime_site = intron_result["five_prime_site"]
    branch_point = intron_result["branch_point"]
    three_prime_site = intron_result["three_prime_site"]

    # --------------------------------------------------
    # 3. SPLICING
    # --------------------------------------------------

    spliced_rna = splice(
        sequence,
        five_prime_site,
        three_prime_site,
    )

    # --------------------------------------------------
    # 4. CAP 5'
    # --------------------------------------------------

    capped_rna = add_cap(spliced_rna)

    # --------------------------------------------------
    # 5. CAUDA POLI-A
    # --------------------------------------------------

    mature_mrna = add_poly_a(capped_rna)

    # --------------------------------------------------
    # RESULTADO
    # --------------------------------------------------

    return {
        "status": "OK",
        "diagnostic": "CORRETO",
        "five_prime_site": five_prime_site,
        "branch_point": branch_point,
        "three_prime_site": three_prime_site,
        "spliced_rna": spliced_rna,
        "mature_mrna": mature_mrna,
    }