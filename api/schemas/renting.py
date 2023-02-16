import pydantic



class RentSchema(pydantic.BaseModel):
    dep: int
    space: int
    amount: float


class RentReturnSchema(pydantic.BaseModel):
    rentSchema: RentSchema
    cities: list
    