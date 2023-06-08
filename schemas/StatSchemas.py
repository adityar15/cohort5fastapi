from pydantic import BaseModel, validator

class StatCreateRequest(BaseModel):
    stat_name: str
    stat_value: str
    extraPrice: int

    @validator('stat_value')
    def check_for_max_50_chars(cls, v):
        if len(v) > 50:
            raise ValueError('stat value must not be more than 50 characters')
        return v