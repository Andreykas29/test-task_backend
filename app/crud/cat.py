from sqlalchemy.orm import Session
from app.models.cat import Cat
from app.schemas.cat import CatCreate

def get_cat(db: Session, cat_id: int):
    return db.query(Cat).filter(Cat.id == cat_id).first()

def get_cats(db: Session):
    return db.query(Cat).all()

def create_cat(db: Session, cat: CatCreate):
    db_cat = Cat(**cat.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def update_cat_salary(db: Session, cat_id: int, new_salary: float):
    cat = get_cat(db, cat_id)
    if cat:
        cat.salary = new_salary
        db.commit()
        db.refresh(cat)
    return cat

def delete_cat(db: Session, cat_id: int):
    cat = get_cat(db, cat_id)
    if cat:
        db.delete(cat)
        db.commit()
        return True
    return False
