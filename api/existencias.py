from fastapi import APIRouter, HTTPException, Depends
from services.existencias_service import get_existencias
from domain.existencia import ExistenciasResponse
from core.security import validate_api_key

router = APIRouter()


@router.get("/existencias", response_model=ExistenciasResponse)
def listar_existencias(api_key: str = Depends(validate_api_key)):
    try:
        data = get_existencias()
        return {"status": "ok", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
