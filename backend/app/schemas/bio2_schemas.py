from pydantic import BaseModel

class RNAProcessingRequest(BaseModel):
    sequence: str

class RNAProcessingResponse(BaseModel):
    status: str
    diagnostic: str

    five_prime_site: int | None = None
    branch_point: int | None = None
    three_prime_site: int | None = None

    spliced_rna: str | None = None
    mature_mrna: str | None = None