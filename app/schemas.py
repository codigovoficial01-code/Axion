from pydantic import BaseModel
from datetime import datetime

class SaleCreate(BaseModel):
    product_name: str
    category: str
    revenue: float
    quantity: int

class SaleResponse(SaleCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
