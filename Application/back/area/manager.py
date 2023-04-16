from sqlalchemy.orm import Session
import uuid
from database import model, schemas
#from sheets.manager import execute


def get_product_by_name(db: Session, name: str):
    return db.query(model.Area).filter(model.Area.name == name).first()

def get_all (db: Session):
    return db.query(model.Area).all()

def create_product(db: Session, area: schemas.Area):

    find_product = db.query(model.Area).filter(model.Area.account_id == area.account_id).first()    
    user = db.query(model.Account).filter(model.Account.id == area.account_id).first()
    
    if not find_product:
        user.first_date_product_register = area.register_date
        user.last_date_product_register = area.register_date
        user.amount_product += area.amount
        user.amount_register_product += 1

    if user and find_product:
        user.last_date_product_register = area.register_date
        user.amount_product += area.amount
        user.amount_register_product += 1
    
    db_product = model.Area(
        id = uuid.uuid4().hex,
        name = area.name,
        amount = area.amount,
        value = area.value,
        register_date = area.register_date,
        account_id = area.account_id
        )

    

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    #execute()

    return db_product