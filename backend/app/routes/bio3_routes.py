from io import BytesIO

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from fastapi.responses import StreamingResponse

from app.schemas.bio3_schemas import (
    RibosomeRequest,
    RibosomeResponse
)

from app.services.biocompiler3.ribosome_processor import ( process_mature_mrna )
from app.services.biocompiler3.text_report_translate import ( generate_text_report )

router = APIRouter(
    prefix="/bio3",
    tags=["BioCompiler 3.0"],
)

@router.post(
    "/translate",
    response_model=RibosomeResponse
)

def translate_single_sequence( request: RibosomeRequest ):

    return process_mature_mrna( request.sequence )

@router.post("/translate/file")
async def translate_file(
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

        result = process_mature_mrna( sequence )

        result["line"] = line_number

        results.append(result)

    return {
        "total": len(results),
        "results": results
    }


@router.post("/translate/file/report")
async def generate_file_report(
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

        result = process_mature_mrna( sequence )

        result["line"] = line_number

        results.append(result)

    report = generate_text_report( results )

    report_bytes = BytesIO( report.encode("utf-8"))

    return StreamingResponse(
        report_bytes,
        media_type="text/plain",
        headers={
            "Content-Disposition":
            "attachment; filename=relatorio_biocompiler3.txt"
        }
    )