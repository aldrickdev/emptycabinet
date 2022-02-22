from datetime import datetime, timedelta
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from emptycabinet.data.schemas.users import Token, TokenData, User

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5

# password
fake_db = {
    "aldrick": {
        "username": "aldrick",
        "hashed_password": "$2b$12$4gYAcadijRFrw5m5JRlzpeifT7V.tJjAStRqVpyGQpfe5Q1gO8BaS",
    },
    "daphne": {
        "username": "daphne",
        "hashed_password": "$2b$12$4gYAcadijRFrw5m5JRlzpeifT7V.tJjAStRqVpyGQpfe5Q1gO8BaS",
    },
    "jelitza": {
        "username": "jelitza",
        "hashed_password": "$2b$12$4gYAcadijRFrw5m5JRlzpeifT7V.tJjAStRqVpyGQpfe5Q1gO8BaS",
    },
}

router = APIRouter()

# oauth2_scheme will either get the token from the request or
#     will need the user to login to create a token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


# checks if user can has access to the resource
async def get_user(token: str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception

        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user_w_username(username=token_data.username)

    if not user:
        raise credentials_exception

    return user


def get_user_w_username(username: str) -> User:
    user = fake_db[username]
    return User(**user)


def authenticate_user(username: str, password: str) -> User | None:
    user_in_db = fake_db[username]
    print(user_in_db)

    if not user_in_db:
        return None

    if not verify_password(password, user_in_db["hashed_password"]):
        return None

    return User(**user_in_db)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


# If a token is not provided, this will run to create a token if the user is valid
@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    entered_creds = {"username": form_data.username, "password": form_data.password}

    # check if the user is in the Database
    user = authenticate_user(entered_creds["username"], entered_creds["password"])

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
