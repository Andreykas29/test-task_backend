from sqlalchemy.orm import Session
from app.models import mission, goal
from app.schemas import mission as mission_schema

def create_mission_with_goals(db: Session, mission_in: mission_schema.MissionCreate):
    db_mission = mission.Mission(status=mission_in.status, cat_id=mission_in.cat_id)
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)

    for goal_in in mission_in.goals:
        db_goal = goal.Goal(
            mission_id=db_mission.id,
            name=goal_in.name,
            country=goal_in.country,
            notes=goal_in.notes or "",
            is_done=goal_in.is_done or False,
        )
        db.add(db_goal)

    db.commit()
    db.refresh(db_mission)
    return db_mission

def get_mission(db: Session, mission_id: int):
    return db.query(mission.Mission).filter(mission.Mission.id == mission_id).first()

def get_missions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(mission.Mission).offset(skip).limit(limit).all()

def delete_mission(db: Session, mission_id: int):
    m = get_mission(db, mission_id)
    if not m:
        return None
    if m.cat_id is not None:
        raise Exception("Cannot delete mission assigned to a cat")
    db.delete(m)
    db.commit()
    return m

def update_mission_goals(db: Session, mission_id: int, goals_in: list[mission_schema.GoalCreate]):
    m = get_mission(db, mission_id)
    if not m:
        return None

    for g in m.goals:
        db.delete(g)
    db.commit()

    for g_in in goals_in:
        g = goal.Goal(
            mission_id=mission_id,
            name=g_in.name,
            country=g_in.country,
            notes=g_in.notes or "",
            is_done=g_in.is_done or False,
        )
        db.add(g)
    db.commit()
    db.refresh(m)
    return m

def mark_goal_done(db: Session, goal_id: int):
    g = db.query(goal.Goal).filter(goal.Goal.id == goal_id).first()
    if not g:
        return None
    g.is_done = True
    db.commit()
    db.refresh(g)
    return g

def update_goal_notes(db: Session, goal_id: int, notes: str):
    g = db.query(goal.Goal).filter(goal.Goal.id == goal_id).first()
    if not g:
        return None
    if g.is_done or (g.mission and g.mission.status == "completed"):
        raise Exception("Cannot edit notes on completed goal or mission")
    g.notes = notes
    db.commit()
    db.refresh(g)
    return g

def assign_cat_to_mission(db: Session, mission_id: int, cat_id: int):
    m = get_mission(db, mission_id)
    if not m:
        return None
    m.cat_id = cat_id
    db.commit()
    db.refresh(m)
    return m
