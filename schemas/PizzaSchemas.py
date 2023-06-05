from pydantic import BaseModel, validator

class PizzaCreateRequest(BaseModel):
    name: str
    description: str
    basePrice: int

    @validator('description')
    def check_for_min_10_chars(cls, v):
        if len(v) < 10:
            raise ValueError('description must be at least 10 characters')
        return v
    
    