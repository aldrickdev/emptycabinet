from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext
from pydantic import BaseModel

from emptycabinet.dependencies.user_auth import get_user

router = APIRouter()

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    hashed_password: str


@router.get("/users/{username}/cabinets")
async def get_users_cabinets(username: str, current_user: User = Depends(get_user)):
    print("Getting Users Cabinets...")
    return {"cabinet_ids": ["1", "2", "3"]}
