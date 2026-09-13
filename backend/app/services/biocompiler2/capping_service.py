from app.core.constants import CAP_5


def add_cap(sequence: str) -> str:
    """
    Adiciona o marcador didático m7Gppp
    na extremidade 5' do RNA.
    """

    return CAP_5 + sequence