"""
ARQUIVO 4 DO BIOCOMPILER 2.0
Remove o intron delimitado pelo sítio GU e pelo sítio AG.
O GU e o AG também são removidos.
Retorna a sequência com os éxons unidos.
"""

def splice(
    sequence: str,
    five_prime_site: int,
    three_prime_site: int,
) -> str:


    intron_start = five_prime_site
    intron_end = three_prime_site + 2

    return (
        sequence[:intron_start]
        + sequence[intron_end:]
    )