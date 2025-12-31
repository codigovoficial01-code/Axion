from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes.sales import router as sales_router
from app.routes.analysis import router as analysis_router

app = FastAPI(title="AXION")

# Rotas da API
app.include_router(sales_router, prefix="/sales", tags=["Sales"])
app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Servir o frontend no ROOT
@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")
