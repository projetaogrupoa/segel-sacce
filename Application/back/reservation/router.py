from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from database import  schemas
from reservation import manager
from database.database import get_db
from auth.manager import get_current_user

router = APIRouter(
    prefix="/reservations",
    tags=["reservation"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=schemas.Reservation)
def create_Order(reservation: schemas.Reservation, db: Session = Depends(get_db)):
    db_order = manager.avaiable_product(db, area_id=reservation.area_id, amount=reservation.amount)
    if db_order is None:
        raise HTTPException(status_code=400, detail="Product amount is not avaiable try again.")
    return manager.create_order(db=db, reservation=reservation)

@router.get("/list", response_model=List[schemas.Reservation])
def read_users(db: Session = Depends(get_db)):
    orders = manager.get_all(db)
    return orders