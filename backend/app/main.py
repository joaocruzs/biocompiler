from fastapi import FastAPI

from app.routes.analysis_routes import router as analysis_router


app = FastAPI(
    title="BioCompiler API",
    description="API para análise de sequências genéticas DNA → RNA",
    version="1.0.0"
)


app.include_router(analysis_router)


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