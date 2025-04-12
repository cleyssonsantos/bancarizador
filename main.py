from fastapi import FastAPI
from src.routes.oferta import viewer

app = FastAPI(
    title="Bancarizador API",
    description="MVP para integração com múltiplos bancarizadores utilizando Clean Architecture + Adapter",
    version="1.0.0"
)

app.include_router(viewer.router, prefix="/api/v1")
