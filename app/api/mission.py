from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas import mission as mission_schema
from app.schemas import goal as goal_schema
from app.crud import mission as mission_crud
from app.dependencies import get_db  

router = APIRouter()

@router.post("/", response_model=mission_schema.Mission)
def create_mission(mission_in: mission_schema.MissionCreate, db: Session = Depends(get_db)):
    return mission_crud.create_mission_with_goals(db, mission_in)

@router.get("/", response_model=List[mission_schema.Mission])
def list_missions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return mission_crud.get_missions(db, skip=skip, limit=limit)

@router.get("/{mission_id}", response_model=mission_schema.Mission)
def get_mission(mission_id: int, db: Session = Depends(get_db)):
    mission_obj = mission_crud.get_mission(db, mission_id)
    if not mission_obj:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission_obj

@router.delete("/{mission_id}", response_model=mission_schema.Mission)
def delete_mission(mission_id: int, db: Session = Depends(get_db)):
    try:
        mission_obj = mission_crud.delete_mission(db, mission_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not mission_obj:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission_obj

@router.put("/{mission_id}/goals", response_model=mission_schema.Mission)
def update_goals(mission_id: int, goals: List[mission_schema.GoalCreate], db: Session = Depends(get_db)):
    mission_obj = mission_crud.update_mission_goals(db, mission_id, goals)
    if not mission_obj:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission_obj

@router.patch("/goal/{goal_id}/done", response_model=goal_schema.Goal)
def mark_goal_done(goal_id: int, db: Session = Depends(get_db)):
    goal_obj = mission_crud.mark_goal_done(db, goal_id)
    if not goal_obj:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal_obj

@router.patch("/goal/{goal_id}/notes", response_model=goal_schema.Goal)
def update_goal_notes(goal_id: int, notes: goal_schema.GoalUpdate, db: Session = Depends(get_db)):
    if notes.notes is None:
        raise HTTPException(status_code=400, detail="Notes required")
    try:
        goal_obj = mission_crud.update_goal_notes(db, goal_id, notes.notes)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not goal_obj:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal_obj

@router.patch("/{mission_id}/assign_cat/{cat_id}", response_model=mission_schema.Mission)
def assign_cat(mission_id: int, cat_id: int, db: Session = Depends(get_db)):
    mission_obj = mission_crud.assign_cat_to_mission(db, mission_id, cat_id)
    if not mission_obj:
        raise HTTPException(status_code=404, detail="Mission or Cat not found")
    return mission_obj
