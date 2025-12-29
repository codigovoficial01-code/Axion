from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import generate_decisions

router = APIRouter(prefix="/analysis", tags=["Decision Analysis"])

@router.get("/weekly-decisions")
def weekly_decisions(db: Session = Depends(get_db)):
    return generate_decisions(db)
