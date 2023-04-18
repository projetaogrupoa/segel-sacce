from sqlalchemy.orm import Session
import uuid
from database import model, schemas
# from sheets.manager import execute


def get_product_by_name(db: Session, name: str):
    return db.query(model.Area).filter(model.Area.name == name).first()


def get_all(db: Session):
    return db.query(model.Area).all()


def create_area(db: Session, area: schemas.Area):

    user = db.query(model.Account).filter(
        model.Account.id == area.account_id).first()

    if not user:
        area.account_id = None

    else:
        area.account_id = user.id

    db_area = model.Area(
        id=uuid.uuid4().hex,
        name=area.name,
        description=area.description,
        available=area.available,
        account_id=area.account_id
    )

    db.add(db_area)
    db.commit()
    db.refresh(db_area)

    # execute()

    return db_area
