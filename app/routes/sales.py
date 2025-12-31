from fastapi import APIRouter
from app.database import get_db
from datetime import datetime

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/")
def create_sale(sale: dict):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sales (product_name, category, revenue, quantity, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        sale["product"],
        sale["category"],
        float(sale["revenue"]),
        int(sale["quantity"]),
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    return {"status": "Venda cadastrada com sucesso"}

@router.get("/")
def list_sales():
    conn = get_db()
    cursor = conn.cursor()

    rows = cursor.execute("SELECT * FROM sales").fetchall()
    return [dict(row) for row in rows]

@router.get("/decisions")
def generate_decisions():
    conn = get_db()
    cursor = conn.cursor()

    total = cursor.execute(
        "SELECT SUM(revenue * quantity) FROM sales"
    ).fetchone()[0] or 0

    return {
        "total_sales": total,
        "decision": "Aumentar estoque dos produtos mais vendidos"
    }
