from pydantic import BaseModel
from typing import Optional

class GoalBase(BaseModel):
    name: str
    country: str
    notes: Optional[str] = ""
    is_done: Optional[bool] = False

class GoalCreate(GoalBase):
    pass

class GoalUpdate(BaseModel):
    notes: Optional[str] = None
    is_done: Optional[bool] = None

class Goal(GoalBase):
    id: int

    class Config:
        orm_mode = True
