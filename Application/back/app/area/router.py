from typing import List
from fastapi import Depends, Query
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from database import schemas
from area import manager
from database.database import get_db


router = APIRouter(
    prefix="/area",
    tags=["Area"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=schemas.Area)
def create_area(area: schemas.Area, db: Session = Depends(get_db)):
    db_product = manager.get_product_by_name(db, name=area.name)
    if db_product:
        raise HTTPException(
            status_code=400, detail="Area already registered")
    return manager.create_area(db=db, area=area)


@router.get("/list", response_model=List[schemas.Area])
def read_users(db: Session = Depends(get_db)):
    users = manager.get_all(db)
    return users
