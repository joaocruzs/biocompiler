"""
Biocompiler 2.0 - Rotas
"""

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import PlainTextResponse
from app.schemas.bio2_schemas import (
    RNAProcessingRequest,
    RNAProcessingResponse,
)
from app.services.biocompiler2.rna_processor import ( process_pre_mrna,)
from app.services.biocompiler2.text_report_generate import ( generate_text_report, )

router = APIRouter(
    prefix="/bio2",
    tags=["BioCompiler 2.0"],
)

@router.post(
    "/generate",
    response_model=RNAProcessingResponse,
)
def process_rna(request: RNAProcessingRequest):
    result = process_pre_mrna(request.sequence)
    return result

@router.post("/generate/file")
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
    "/generate/file/report",
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

    report = generate_text_report(results)

    return PlainTextResponse(
        content=report,
        media_type="text/plain; charset=utf-8",
        headers={
            "Content-Disposition":
                'attachment; filename="relatorio_biocompiler2.txt"'
        },
    )