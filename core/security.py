from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

API_KEY = "3urore@5"
API_KEY_NAME = "EuroreAPIKey"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def validate_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=403, detail="Acceso denegado: Ingrese la clave correcta."
        )
    return api_key
