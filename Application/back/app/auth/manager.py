from sqlalchemy.orm import Session
from database import model, schemas
import uuid
from decouple import config
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext


SECRET = config("SECRET_KEY")

SECRET_KEY = SECRET
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/account/sign-in",
                                     scheme_name="JWT"
                                     )


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_account(db: Session, email: str):
    return db.query(model.Account).filter(model.Account.email == email).first()


def authenticate_user(db: Session, email: str, password: str):
    user = get_account(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
        return token_data
    except JWTError:
        raise credentials_exception


async def get_current_active_user(current_user: schemas.Account = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_account_by_email(db: Session, email: str):
    return db.query(model.Account).filter(model.Account.email == email).first()


def create_account(db: Session, account: schemas.Account):
    db_account = model.Account(
        id=uuid.uuid4().hex,
        email=account.email,
        hashed_password=get_password_hash(account.hashed_password),
        cpf=account.cpf,
        name=account.name,
        user_type=account.user_type,
        available=account.available,
        phone_number=account.phone_number
    )

    db.add(db_account)
    db.commit()
    db.refresh(db_account)

    return db_account
