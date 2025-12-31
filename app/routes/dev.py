from fastapi import APIRouter
from app.database import get_db

router = APIRouter(prefix="/dev", tags=["Dev"])

@router.delete("/reset-database")
def reset_database():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sales")
    conn.commit()

    return {"status": "Banco de dados resetado com sucesso"}
