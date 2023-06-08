from pydantic import BaseModel, validator

class ToppingCreateRequest(BaseModel):
    name: str
    description: str
    extraPrice: int

    @validator('description')
    def check_for_max_100_chars(cls, v):
        if len(v) > 100:
            raise ValueError('description must not be more than 100 characters')
        return v