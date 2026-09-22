from io import BytesIO

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from fastapi.responses import StreamingResponse

from app.schemas.bio2_schemas import (
    RNAProcessingRequest,
    RNAProcessingResponse
)

from app.services.biocompiler2.rna_processor import ( process_pre_mrna )
from app.services.biocompiler2.text_report_generate import ( generate_text_report )

router = APIRouter(
    prefix="/bio2",
    tags=["BioCompiler 2.0"],
)

@router.post(
    "/generate",
    response_model=RNAProcessingResponse
)
def process_rna( request: RNAProcessingRequest ):

    return process_pre_mrna( request.sequence )

@router.post( "/generate/file")
async def process_rna_file(
    file: UploadFile = File(...)
):

    content = await file.read()

    text = content.decode("utf-8")

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

        result = process_pre_mrna( sequence )

        results.append({
            "line": line_number,
            "sequence": sequence,
            **result,
        })

    return {
        "total": len(results),
        "results": results,
    }


@router.post( "/generate/file/report" )
async def process_rna_file_report(
    file: UploadFile = File(...)
):

    content = await file.read()

    text = content.decode("utf-8")

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

        result = process_pre_mrna( sequence )

        results.append({
            "line": line_number,
            "sequence": sequence,
            **result,
        })

    report = generate_text_report( results )

    report_bytes = BytesIO(
        report.encode("utf-8")
    )

    return StreamingResponse(
        report_bytes,
        media_type="text/plain",
        headers={
            "Content-Disposition":
                "attachment; "
                "filename=relatorio_biocompiler2.txt"
        }
    )