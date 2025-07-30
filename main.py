from fastapi import FastAPI
from api import existencias, system

app = FastAPI(
    title="EuroRepuestos API",
    description="API para consultar existencias de productos desde Odoo",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
)

# Routers
app.include_router(system.router, tags=["System"])
app.include_router(existencias.router, prefix="/existencias", tags=["Existencias"])
