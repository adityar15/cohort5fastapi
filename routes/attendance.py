from fastapi import APIRouter, Depends
from schemas.UserSchema import UserLoginRequest, UserRegisterRequest
from sqlalchemy.orm import Session
from database_configs.connection import get_db
from services.UserService import UserService

router = APIRouter(
    prefix="/attendance",
    tags=["attendance"],
)

@router.post("/signin")
def asasd():
    pass

@router.post("/signup")
def register(registerPayload: UserRegisterRequest, db: Session = Depends(get_db)):
    userService = UserService(db)
    registeredUser = userService.createUser(registerPayload)
    return registeredUser

    