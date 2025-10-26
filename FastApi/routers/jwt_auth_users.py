from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext


router = APIRouter(
    prefix="/jwt-auth-users",
    tags=["jwt-auth-users"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="autoh_basic")

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserInDB(User):
    hashed_password: str

users_db = {
    "johndoe": {
        "username": "johndoe",
        "fullname": "John Doe",
        "email": "johndoe@example.com",
        "disabled": False,
        "hashed_password": "fakehashedsecret"
    },
    "alice": {
        "username": "alice",
        "fullname": "Alice Wonderson",
        "email": "alice@example.com",
        "disabled": True,
        "hashed_password": "fakehashedsecret2"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserInDB(**users_db[username])
    return None

@router.post("/jwt_auth_users")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    user = search_user_db(form_data.username)

    if not form_data.password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    return {"access_token": user.username, "token_type": "bearer"}