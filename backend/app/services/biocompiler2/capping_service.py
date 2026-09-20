from app.core.constants import CAP_5

"""
ARQUIVO 5 DO BIOCOMPILER 2.0
Adiciona o marcador didático m7Gppp
na extremidade 5' do RNA.
"""

def add_cap(sequence: str) -> str:

    return CAP_5 + sequence