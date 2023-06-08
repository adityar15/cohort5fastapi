from pydantic import BaseModel, validator
from typing import Optional

class PizzaCreateRequest(BaseModel):
    name: str
    description: str
    basePrice: int
    toppings: list[int]
    stats: Optional[list[int]] = []

    @validator('description')
    def check_for_min_10_chars(cls, v):
        if len(v) < 10:
            raise ValueError('description must be at least 10 characters')
        return v
    


# this is a response model i.e the model that will be returned to the client
# this helps to shape our response to the client
class PizzaResponseModel(BaseModel):
    name: str
    description: str
    basePrice: int
    toppings: list
    # what if the pizza does not have any stats?
    # we can make the stats optional by using the Optional type from typing
    # make sure to add typing to the import statement (line 2)
    # make sure to add it in requirements.txt
    stats: Optional[list] = []

# as this model returns the SQLAlchemy model object, we need to tell Pydantic to use the ORM mode
    class Config:
        orm_mode = True