from sqlalchemy.orm import Session
import uuid
from fastapi import HTTPException
from database import model, schemas
# from sheets.manager import execute


def get_orders_by_product(db: Session, area_id: str):
    return db.query(model.Reservation).filter(model.Reservation.area_id == area_id).all()


def get_all(db: Session):
    return db.query(model.Reservation).all()


def avaiable_product(db: Session, area_id: str, amount: int):

    avaiable_product = db.query(model.Reservation).filter(
        model.Reservation.id == area_id).first()

    if avaiable_product.amount >= amount:
        return avaiable_product

    elif avaiable_product.amount < amount:
        return None


def create_reservation(db: Session, reservation: schemas.Reservation):

    user = db.query(model.Account).filter(
        model.Account.id == reservation.account_id).first()

    area = db.query(model.Area).filter(
        model.Area.id == reservation.area_id).first()

    if user and area:

        db_order = model.Reservation(
            id=uuid.uuid4().hex,
            value=reservation.value,
            reservation_date=reservation.reservation_date,
            time_start=reservation.time_start,
            time_end=reservation.time_end,
            justification=reservation.justification,
            user_type=reservation.user_type,
            status=reservation.status,
            area_id=reservation.area_id,
            account_id=reservation.account_id
        )

        db.add(db_order)
        db.commit()
        db.refresh(db_order)

        # execute()

        return db_order
    else:
        return None
