"""
ARQUIVO 5 DO BIOCOMPILER 2.0
Adiciona o marcador didático m7Gppp
na extremidade 5' do RNA.
"""

from app.core.constants import CAP_5

def add_cap(sequence: str) -> str:

    return CAP_5 + sequence