from app.core.constants import SPLICE_SITE_5, SPLICE_SITE_3


def find_five_prime_sites(sequence: str) -> list[int]:
    """
    Encontra todas as ocorrências do sítio 5' (GU).
    Retorna os índices onde cada GU começa.
    """

    positions = []

    start = 0

    while True:
        position = sequence.find(SPLICE_SITE_5, start)

        if position == -1:
            break

        positions.append(position)
        start = position + 1

    return positions


def find_three_prime_sites(sequence: str) -> list[int]:
    """
    Encontra todas as ocorrências do sítio 3' (AG).
    Retorna os índices onde cada AG começa.
    """

    positions = []

    start = 0

    while True:
        position = sequence.find(SPLICE_SITE_3, start)

        if position == -1:
            break

        positions.append(position)
        start = position + 1

    return positions