from typing import Optional
from pydantic import BaseModel

class SequenceRequest(BaseModel):
    sequence: str

class AnalysisResponse(BaseModel):
    line: Optional[int] = None

    sequence: str
    status: str

    start_position: Optional[int] = None
    stop_position: Optional[int] = None
    stop_codon: Optional[str] = None

    mrna: Optional[str] = None

class BatchAnalysisResponse(BaseModel):
    total_sequences: int
    results: list[AnalysisResponse]
    summary: dict