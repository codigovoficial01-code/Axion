from fastapi import APIRouter
from app.services import list_sales

router = APIRouter()

@router.get("/weekly-decisions")
def generate_decisions():
    sales = list_sales()

    if not sales:
        return {"decision": "Insira vendas para gerar decisões."}

    total = sum(s.revenue for s in sales)

    return {
        "decision": f"Você faturou R$ {total:.2f}. Considere escalar os produtos mais vendidos."
    }
