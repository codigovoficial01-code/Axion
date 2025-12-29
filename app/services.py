from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Sale
from app.schemas import SaleCreate

# -------------------------
# SALES
# -------------------------

def create_sale(db: Session, sale: SaleCreate):
    db_sale = Sale(
        product_name=sale.product_name,
        category=sale.category,
        revenue=sale.revenue,
        quantity=sale.quantity
    )
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale


def get_sales(db: Session):
    return db.query(Sale).order_by(Sale.created_at.desc()).all()


# -------------------------
# ANALYSIS
# -------------------------

def generate_decisions(db: Session):
    total_sales = db.query(func.count(Sale.id)).scalar()
    total_revenue = db.query(func.sum(Sale.revenue)).scalar() or 0
    total_quantity = db.query(func.sum(Sale.quantity)).scalar() or 0

    decisions = []

    if total_sales == 0:
        decisions.append("Nenhuma venda registrada ainda.")
    else:
        decisions.append(f"{total_sales} vendas registradas.")
        decisions.append(f"Receita total: R$ {total_revenue:.2f}")
        decisions.append(f"Quantidade total vendida: {total_quantity}")

        if total_revenue < 1000:
            decisions.append("Foque em aumentar ticket médio ou volume.")
        else:
            decisions.append("Receita saudável. Avalie escala de tráfego.")

    return {
        "total_sales": total_sales,
        "total_revenue": total_revenue,
        "total_quantity": total_quantity,
        "decisions": decisions
    }
