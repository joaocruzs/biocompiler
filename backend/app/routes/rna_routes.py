"""
Biocompiler 2.0 - Rotas
"""

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import PlainTextResponse
from app.schemas.rna_schemas import (
    RNAProcessingRequest,
    RNAProcessingResponse,
)
from app.services.biocompiler2.rna_processor import (
    process_pre_mrna,
)

router = APIRouter(
    prefix="/rna",
    tags=["BioCompiler 2.0 - RNA Processor"],
)

@router.post(
    "/process",
    response_model=RNAProcessingResponse,
)
def process_rna(request: RNAProcessingRequest):
    result = process_pre_mrna(request.sequence)
    return result

@router.post("/process/file")
async def process_rna_file(
    file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="O arquivo deve ser .txt"
        )

    content = await file.read()

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="O arquivo deve estar em UTF-8"
        )

    sequences = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    results = []

    for line_number, sequence in enumerate(
        sequences,
        start=1
    ):
        result = process_pre_mrna(sequence)

        results.append({
            "line": line_number,
            "sequence": sequence,
            **result,
        })

    return {
        "total": len(results),
        "results": results,
    }


@router.post(
    "/process/file/report",
    response_class=PlainTextResponse,
)
async def process_rna_file_report(
    file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="O arquivo deve ser .txt"
        )

    content = await file.read()

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="O arquivo deve estar em UTF-8"
        )

    sequences = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    report_lines = [
        "linha;status;resultado;mRNA_maduro"
    ]

    for line_number, sequence in enumerate(
        sequences,
        start=1
    ):

        result = process_pre_mrna(sequence)

        status = result["status"]
        diagnostic = result["diagnostic"]

        mature_mrna = (
            result["mature_mrna"]
            if result["mature_mrna"] is not None
            else "NÃO GERADO"
        )

        report_lines.append(
            f"{line_number};"
            f"{status};"
            f"{diagnostic};"
            f"{mature_mrna}"
        )

    report = "\n".join(report_lines)

    return PlainTextResponse(
        content=report,
        media_type="text/plain; charset=utf-8",
        headers={
            "Content-Disposition":
                'attachment; filename="biocompiler_2_report.txt"'
        },
    )