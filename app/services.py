from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base, engine, SessionLocal

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    category = Column(String)
    revenue = Column(Float)
    quantity = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

def create_sale(data):
    db = SessionLocal()
    sale = Sale(**data)
    db.add(sale)
    db.commit()
    db.refresh(sale)
    db.close()
    return sale

def list_sales():
    db = SessionLocal()
    sales = db.query(Sale).all()
    db.close()
    return sales
