from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes.sales import router as sales_router
from app.routes.analysis import router as analysis_router

# Cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AXION",
    description="Decision Intelligence para E-commerce",
    version="0.1.0"
)

# 🔐 CORS (necessário para o frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção, restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "AXION rodando com sucesso 🚀"}

# Rotas
app.include_router(sales_router)
app.include_router(analysis_router)
