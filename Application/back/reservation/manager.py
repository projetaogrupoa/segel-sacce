from sqlalchemy.orm import Session
import uuid
from database import model, schemas
#from sheets.manager import execute

def get_orders_by_product(db: Session, area_id: str):
    return db.query(model.Reservation).filter(model.Reservation.area_id == area_id).all()

def get_all (db: Session):
    return db.query(model.Reservation).all()

def avaiable_product(db: Session, area_id: str, amount: int):

    avaiable_product = db.query(model.Reservation).filter(model.Reservation.id == area_id).first()

    if avaiable_product.amount >= amount:
        return avaiable_product

    elif avaiable_product.amount < amount:
        return None

def create_order(db: Session, reservation: schemas.Reservation):

    find_order = db.query(model.Reservation).filter(model.Reservation.account_id == reservation.account_id).first()

    user = db.query(model.Account).filter(model.Account.id == reservation.account_id).first()

    product = db.query(model.Product).filter(model.Product.id == reservation.area_id).first()

    if product:
        product.amount -= reservation.amount
    
    if not find_order:
        user.first_date_order = reservation.order_date
        user.last_date_order = reservation.order_date
        user.amount_order += reservation.amount
        user.amount_register_order += 1

    if user and find_order:
        user.last_date_order = reservation.order_date
        user.amount_order += reservation.amount
        user.amount_register_order += 1
   
    db_order = model.Reservation(
        id = uuid.uuid4().hex,
        amount = reservation.amount,
        value = reservation.value,
        order_date = reservation.order_date,
        product_id = reservation.product_id,
        account_id = reservation.account_id
        )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    #execute()

    return db_order
