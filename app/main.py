from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from app.routes.sales import router as sales_router
from app.routes.decisions import router as decisions_router

app = FastAPI(title="AXION")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# ROTA PRINCIPAL → INTERFACE
@app.get("/", include_in_schema=False)
def serve_frontend():
    return FileResponse("frontend/index.html")

# API
app.include_router(sales_router, prefix="/api")
app.include_router(decisions_router, prefix="/api")
