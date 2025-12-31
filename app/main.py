from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from app.routes.sales import router as sales_router
from app.routes.decisions import router as decisions_router

app = FastAPI(title="AXION")

# CORS (importante para frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir arquivos estáticos (frontend)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Rota raiz → Interface do Axion
@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")

# Rotas da API
app.include_router(sales_router, prefix="/api")
app.include_router(decisions_router, prefix="/api")
