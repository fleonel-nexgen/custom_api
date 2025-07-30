from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse, summary="Inicio")
async def inicio():
    return """
<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>NexGen ~ EuroRepuestos API</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: #f8f9fa;
                margin: 0;
            }
            .container {
                max-width: 600px;
                margin: 100px auto;
                background: #fff;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                text-align: center;
                position: relative;
            }
            h1 {
                color: #0d6efd;
            }
            a {
                text-decoration: none;
                background: #0d6efd;
                color: white;
                padding: 10px 20px;
                margin: 8px;
                border-radius: 6px;
                display: inline-block;
            }
            a:hover {
                background: #084298;
            }
            footer {
                margin-top: 30px;
                font-size: 13px;
                color: #6c757d;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>EuroRepuestos API</h1>
            <p>Usa el endpoint <b>/existencias</b> para consultar inventarios desde Odoo.</p>
            <a href="/existencias">Existencias</a>
            <a href="/docs">Documentación Swagger</a>
            <a href="/ping">Health Check</a>
            <footer>
                Powered by <b>NexGen</b>
            </footer>
        </div>
    </body>
    </html>
    """


@router.get("/ping", summary="Health Check")
async def ping():
    return {"status": "Ok"}
