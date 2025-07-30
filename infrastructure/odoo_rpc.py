import requests
import os

ODOO_URL = os.getenv(
    "ODOO_URL", "https://eurorepuestos-desarollo-21362196.dev.odoo.com"
)
DB = os.getenv("ODOO_DB", "eurorepuestos-desarollo-21362196")
USERNAME = os.getenv("ODOO_USER", "abner@consult-us.group")
PASSWORD = os.getenv("ODOO_PASS", "Admin123")


def get_uid():
    url = f"{ODOO_URL}/jsonrpc"
    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "common",
            "method": "login",
            "args": [DB, USERNAME, PASSWORD],
        },
        "id": 1,
    }
    response = requests.post(url, json=payload).json()
    if "error" in response:
        raise Exception("Error de autenticación con Odoo")
    return response["result"]


def execute_kw(model, method, args=None, kwargs=None):
    uid = get_uid()
    url = f"{ODOO_URL}/jsonrpc"
    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "object",
            "method": "execute_kw",
            "args": [DB, uid, PASSWORD, model, method, args or [], kwargs or {}],
        },
        "id": 2,
    }
    response = requests.post(url, json=payload).json()
    if "error" in response:
        raise Exception(response["error"])
    return response["result"]
