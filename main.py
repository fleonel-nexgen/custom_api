from fastapi import FastAPI
from api import existencias

app = FastAPI(title="nexgen ~ odoo")

app.include_router(existencias.router)
