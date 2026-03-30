from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    description:str
    value: float