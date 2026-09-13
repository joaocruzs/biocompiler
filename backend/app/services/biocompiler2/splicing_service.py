def splice(
    sequence: str,
    five_prime_site: int,
    three_prime_site: int,
) -> str:
    """
    Remove o intron delimitado pelo sítio GU e pelo sítio AG.

    O GU e o AG também são removidos.

    Retorna a sequência com os éxons unidos.
    """

    intron_start = five_prime_site
    intron_end = three_prime_site + 2

    return (
        sequence[:intron_start]
        + sequence[intron_end:]
    )