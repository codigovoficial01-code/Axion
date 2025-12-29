from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import SaleCreate, SaleResponse
from app import services

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    return services.create_sale(db=db, sale=sale)

@router.get("/", response_model=list[SaleResponse])
def list_sales(db: Session = Depends(get_db)):
    return services.get_sales(db)
