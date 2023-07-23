from pydantic import BaseModel, EmailStr, validator

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

    @validator('password')
    def check_for_length(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        
        elif len(v) > 16:
            raise ValueError('Password must not be more than 16 characters')
        
        return v
    

class UserRegisterRequest(UserLoginRequest):
    name: str