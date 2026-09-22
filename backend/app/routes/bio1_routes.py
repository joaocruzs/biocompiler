from io import BytesIO
from fastapi import (
    APIRouter,
    UploadFile,
    File
)
from fastapi.responses import StreamingResponse
from app.schemas.bio1_schemas import (
    SequenceRequest,
    AnalysisResponse,
    BatchAnalysisResponse
)
from app.services.biocompiler1.sequence_analyzer import ( analyze_sequence )
from app.services.common.file_analysis_service import ( process_uploaded_file )
from app.services.biocompiler1.text_report_transcribe import ( generate_text_report )

router = APIRouter(
    prefix="/bio1",
    tags=["BioCompiler 1.0"],
)

@router.post(
    "/transcribe",
    response_model=AnalysisResponse
)

def analyze_single_sequence( request: SequenceRequest ):

    return analyze_sequence( request.sequence )

@router.post(
    "/transcribe/file",
    response_model=BatchAnalysisResponse
)
async def analyze_file( file: UploadFile = File(...)):

    content = await file.read()

    return process_uploaded_file(
        filename=file.filename,
        content=content
    )

@router.post("/transcribe/file/report")
async def generate_file_report(
    file: UploadFile = File(...)
):

    content = await file.read()

    analysis = process_uploaded_file(
        filename=file.filename,
        content=content
    )

    report = generate_text_report(
        analysis["results"],
        analysis["summary"]
    )

    report_bytes = BytesIO( report.encode("utf-8"))

    return StreamingResponse(
        report_bytes,
        media_type="text/plain",
        headers={
            "Content-Disposition":
            "attachment; filename=relatorio_biocompiler1.txt"
        }
    )