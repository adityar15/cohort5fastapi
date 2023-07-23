from sqlalchemy.orm import Session
from database_configs.models import User
from schemas.UserSchema import UserLoginRequest, UserRegisterRequest
from fastapi import HTTPException
from passlib.context import CryptContext


class UserService:
    def __init__(self, db:Session):
        self.db = db
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def getUserByEmail(self, email:str):
        return self.db.query(User).filter(User.email == email).first()
    
    def createUser(self, requestBody: UserRegisterRequest):
        user = self.getUserByEmail(requestBody.email)  

        if user:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashedPassword = self.pwd_context.hash(requestBody.password)

        addedUser = User(name=requestBody.name, email=requestBody.email, password=hashedPassword, 
                         role="hr")
        self.db.add(addedUser)
        self.db.commit()
        self.db.refresh(addedUser)
        return {
            "email": addedUser.email,
            "id": addedUser.id,
        }