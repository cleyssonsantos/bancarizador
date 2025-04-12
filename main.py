from fastapi import FastAPI
from src.controllers import bancarizador_controller

app = FastAPI(
    title="Bancarizador API",
    description="MVP para integração com múltiplos bancarizadores utilizando Clean Architecture + Adapter",
    version="1.0.0"
)

app.include_router(bancarizador_controller.router, prefix="/v1")
