from app.core.constants import POLY_A_LENGTH

"""
ARQUIVO 6 DO BIOCOMPILER 2.0
Adiciona exatamente 100 adeninas
à extremidade 3' do RNA.
"""

def add_poly_a(sequence: str) -> str:

    return sequence + ("A" * POLY_A_LENGTH)