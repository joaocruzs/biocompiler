from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.bio1_routes import router as analysis_router
from app.routes.bio2_routes import router as rna_router
from app.routes.bio3_routes import router as ribosome_router

app = FastAPI(
    title="BioCompiler API",
    description="API para análise de sequências genéticas DNA → pré-mRNA → mRNA maduro",
    version="3.0.0"
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
app.include_router(ribosome_router)

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