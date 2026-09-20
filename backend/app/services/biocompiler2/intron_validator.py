from app.core.constants import (
    MIN_BRANCH_DISTANCE,
    MAX_BRANCH_DISTANCE,
)
from app.services.biocompiler2.splice_site_detector import (
    find_five_prime_sites,
    find_three_prime_sites,
)

"""
ARQUIVO 3 DO BIOCOMPILER 2.0
Analisa a sequência de pré-mRNA e identifica
se existe um intron válido.

Retorna um dicionário contendo:
    status
    diagnostic
    five_prime_site
    branch_point
    three_prime_site
"""

def validate_intron(sequence: str) -> dict:

    five_prime_sites = find_five_prime_sites(sequence)
    three_prime_sites = find_three_prime_sites(sequence)

    # CASO 2 — sítio 5' ausente

    if not five_prime_sites or five_prime_sites > three_prime_sites:

        if three_prime_sites:
            return {
                "status": "ERRO",
                "diagnostic": "BUG - sítio 5' ausente",
                "five_prime_site": None,
                "branch_point": None,
                "three_prime_site": None,
            }

    # CASO 3 — sítio 3' ausente

    if not three_prime_sites or three_prime_sites < five_prime_sites:

        return {
            "status": "ERRO",
            "diagnostic": "BUG - sítio 3' ausente",
            "five_prime_site": five_prime_sites[0],
            "branch_point": None,
            "three_prime_site": None,
        }

    # Procurar uma combinação GU ... AG

    for five_prime in five_prime_sites:

        compatible_three_prime_sites = [
            position
            for position in three_prime_sites
            if position > five_prime
        ]

        if not compatible_three_prime_sites:
            continue

        for three_prime in compatible_three_prime_sites:

            # Procuramos um A antes do AG.
            for branch_point in range(
                five_prime + 2,
                three_prime
            ):

                if sequence[branch_point] != "A":
                    continue

                distance = three_prime - branch_point

                if (
                    MIN_BRANCH_DISTANCE
                    <= distance
                    <= MAX_BRANCH_DISTANCE
                ):
                    return {
                        "status": "OK",
                        "diagnostic": "CORRETO",
                        "five_prime_site": five_prime,
                        "branch_point": branch_point,
                        "three_prime_site": three_prime,
                    }

    # CASO 4 — branch point inválido

    return {
        "status": "ERRO",
        "diagnostic": "BUG - branch point",
        "five_prime_site": five_prime_sites[0]
        if five_prime_sites
        else None,
        "branch_point": None,
        "three_prime_site": None,
    }