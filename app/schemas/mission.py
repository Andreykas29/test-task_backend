from pydantic import BaseModel
from typing import List, Optional
from app.schemas.goal import Goal, GoalCreate


class MissionBase(BaseModel):
    status: Optional[str] = "active"
    cat_id: Optional[int] = None

class MissionCreate(MissionBase):
    goals: List[GoalCreate]

class MissionUpdate(BaseModel):
    status: Optional[str] = None
    cat_id: Optional[int] = None
    goals: Optional[List[GoalCreate]] = None  

class Mission(MissionBase):
    id: int
    goals: List[Goal]

    class Config:
        orm_mode = True
