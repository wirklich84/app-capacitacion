import os
from fastapi import APIRouter, Body, HTTPException, status, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from models.user import User, UserData
from passlib.context import CryptContext
from pydantic import EmailStr
from dotenv import load_dotenv
load_dotenv()

secret = os.getenv('SECRET_KEY')
cookie = os.getenv('COOKIE_NAME')

manager = LoginManager(secret=secret, token_url='/user/login', use_cookie=True)

manager.cookie_name = cookie

@manager.user_loader()
async def load_user(email : EmailStr):
    user = await User.find_one(User.email == email)
    return user



hash_helper = CryptContext(schemes=["bcrypt"])

async def add_user(new_user: User) -> User:
    user = await new_user.create()
    return user






router_users = APIRouter()

@router_users.post('/new', response_model= UserData)
async def user_singup(user: User = Body(...)):
    user_exists = await User.find_one(User.email == user.email)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email ya registrado!")

    user.password = hash_helper.encrypt(user.password)
    new_user = await add_user(user)
    return new_user

@router_users.post('/login')
async def login(credential: OAuth2PasswordRequestForm = Depends()):
    username = credential.username
    password = credential.password

    user = await load_user(username)

    '''
    if not user:
        raise InvalidCredentialsException
    elif password != user["password"]:
        raise InvalidCredentialsException
    '''

    print(user)