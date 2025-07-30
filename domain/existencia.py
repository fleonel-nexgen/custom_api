from pydantic import BaseModel
from typing import List


class Existencia(BaseModel):
    product_id: int
    product_template_id: int
    nombreProducto: str
    sku: str
    codigoBodega: str
    Bodega: str
    cantidad: float
    reserved_quantity: float


class ExistenciasResponse(BaseModel):
    status: str
    data: List[Existencia]
