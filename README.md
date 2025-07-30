# 🚀 CUSTOM_API

API desarrollada con **FastAPI** que permite consultar existencias de productos directamente desde **Odoo**.  
El servicio está desplegado en **Render** y utiliza **uvicorn** como servidor ASGI.

---

## 📖 Descripción

Este proyecto expone un **endpoint seguro** para consultar inventarios de productos almacenados en Odoo.  
La autenticación se maneja mediante **API Key** enviada en los headers de cada petición.

---

## ⚙️ Desarrollo Local

Sigue estos pasos para ejecutar el proyecto en tu máquina:

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/CUSTOM_API.git
cd CUSTOM_API
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv
```

Activar el entorno:

- Linux / Mac:
  ```bash
  source venv/bin/activate
  ```
- Windows (PowerShell):
  ```powershell
  venv\Scripts\activate
  ```

### 3. Instalar dependencias

Usando el archivo: `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor

```bash
uvicorn main:app --reload
```

Por defecto:

- 🌐 API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- 📑 Documentación Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 📘 Documentación ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔑 Autenticación

Todas las peticiones a la API deben incluir el siguiente header:

EuroreAPIkey: "Clave indicada"

> [!WARNING]
> Consultar con el Administrador las credenciales a usar.

> [!WARNING!]
> Solicita la API Key al **administrador del sistema**.
> Sin este header, la API rechazará la solicitud con un **401 Unauthorized**.

---

## URL Para produccion:

La url para produccion es la siguiente:

```bash
https://custom-api-ev7l.onrender.com/{parametros_abajo_descritos}
```

---

## 📡 Endpoints

### 🔹 `GET /ping`

Verifica el estado del servicio.  
**Ejemplo de respuesta:**

```json
{
  "status": "ok"
}
```

---

### 🔹 `GET /existencias`

Devuelve el inventario de productos desde Odoo.  
**Ejemplo de respuesta:**

```json
{
  "status": "ok",
  "data": [
    {
      "product_id": 123,
      "product_template_id": 456,
      "nombreProducto": "Clavo 2 pulgadas",
      "sku": "CLV-002",
      "codigoBodega": "BOD-01",
      "Bodega": "Bodega Central",
      "cantidad": 300,
      "reserved_quantity": 20
    }
  ]
}
```

---

## ☁️ Configuración en Render

Para desplegar el proyecto en **Render**:

- **Lenguaje:** Python 3
- **Build Command:**
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command:**
  ```bash
  uvicorn main:app --host 0.0.0.0 --port $PORT
  ```
- **Nota:**
  - Render asigna automáticamente el puerto a través de la variable `$PORT`.
  - El archivo `main.py` debe estar en la raíz del proyecto, **no en una carpeta `app/`**.

---

## 🔒 Notas de Seguridad

⚠️ **Recomendaciones importantes**:

- Durante pruebas, la **API Key** puede estar **hardcodeada** en el código.
- Habilita siempre **HTTPS** para proteger el tráfico de la API.
- Revoca inmediatamente cualquier clave comprometida.

---

## 📌 Tecnologías Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://requests.readthedocs.io/)
- [Render](https://render.com/)

---

## 👨‍💻 Autor

**CUSTOM_API** – Desarrollado para integraciones con Odoo.
