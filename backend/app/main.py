from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.analysis_routes import router as analysis_router
from app.routes.rna_routes import router as rna_router

app = FastAPI(
    title="BioCompiler API",
    description="API para análise de sequências genéticas DNA → pré-mRNA → mRNA maduro",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis_router)
app.include_router(rna_router)

@app.get("/")
def root():
    return {
        "message": "BioCompiler API está funcionando"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }