from pydantic import BaseModel


class RibosomeRequest(BaseModel):
    sequence: str


class RibosomeResponse(BaseModel):
    status: str
    diagnostic: str
    protein: str | None = None