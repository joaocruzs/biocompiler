from io import BytesIO

from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import PlainTextResponse

from app.schemas.bio3_schemas import (
    RibosomeRequest,
    RibosomeResponse,
)

from app.services.biocompiler3.ribosome_processor import (
    process_mature_mrna,
)


router = APIRouter(
    prefix="/bio3",
    tags=["BioCompiler 3.0 - Sr. Ribossomo"],
)


# ============================================================
# PROCESSAMENTO DE UMA SEQUÊNCIA
# ============================================================

@router.post(
    "/translate",
    response_model=RibosomeResponse,
)
def process_sequence(request: RibosomeRequest):
    """
    Processa uma sequência de mRNA maduro.
    """

    sequence = request.sequence.strip()

    if not sequence:
        raise HTTPException(
            status_code=400,
            detail="A sequência não pode estar vazia.",
        )

    result = process_mature_mrna(sequence)

    return result


# ============================================================
# PROCESSAMENTO DE ARQUIVO
# ============================================================

@router.post(
    "/translate/file",
)
async def process_file(
    file: UploadFile = File(...),
):
    """
    Processa um arquivo TXT contendo uma sequência por linha.
    """

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Nome do arquivo não informado.",
        )

    if not file.filename.lower().endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Apenas arquivos .txt são permitidos.",
        )

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="O arquivo está vazio.",
        )

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Erro ao ler o arquivo. Utilize UTF-8.",
        )

    sequences = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not sequences:
        raise HTTPException(
            status_code=400,
            detail="Nenhuma sequência encontrada no arquivo.",
        )

    results = []

    for line_number, sequence in enumerate(sequences, start=1):
        result = process_mature_mrna(sequence)

        result["line"] = line_number

        results.append(result)

    return {
        "total": len(results),
        "results": results,
    }


# ============================================================
# PROCESSAMENTO DE ARQUIVO COM RELATÓRIO TABULAR
# ============================================================

@router.post(
    "/translate/file/report",
    response_class=PlainTextResponse,
)
async def process_file_report(
    file: UploadFile = File(...),
):
    """
    Processa um arquivo TXT e retorna um relatório tabular.

    Formato:

    linha;status;resultado;proteina
    """

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Nome do arquivo não informado.",
        )

    if not file.filename.lower().endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Apenas arquivos .txt são permitidos.",
        )

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="O arquivo está vazio.",
        )

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Erro ao ler o arquivo. Utilize UTF-8.",
        )

    sequences = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not sequences:
        raise HTTPException(
            status_code=400,
            detail="Nenhuma sequência encontrada no arquivo.",
        )

    report_lines = [
        "linha;status;resultado;proteina"
    ]

    for line_number, sequence in enumerate(sequences, start=1):
        result = process_mature_mrna(sequence)

        status = result.get("status", "ERRO")
        diagnostic = result.get(
            "diagnostic",
            "Erro desconhecido",
        )

        protein = result.get("protein")

        if protein is None:
            protein = "NÃO GERADA"

        report_line = (
            f"{line_number};"
            f"{status};"
            f"{diagnostic};"
            f"{protein}"
        )

        report_lines.append(report_line)

    report = "\n".join(report_lines)

    return report