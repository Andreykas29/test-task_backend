from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.cat import CatCreate, CatRead, CatUpdateSalary
from app.crud.cat import create_cat, get_cat, get_cats, update_cat_salary, delete_cat
from app.dependencies import get_db
from app.services.cat import validate_breed

router = APIRouter()

@router.post("/", response_model=CatRead, status_code=status.HTTP_201_CREATED)
async def create_cat_endpoint(cat: CatCreate, db: Session = Depends(get_db)):
    is_valid_breed = await validate_breed(cat.breed)
    if not is_valid_breed:
        raise HTTPException(status_code=400, detail="Invalid cat breed")
    return create_cat(db, cat)

@router.get("/", response_model=list[CatRead])
def read_cats(db: Session = Depends(get_db)):
    return get_cats(db)

@router.get("/{cat_id}", response_model=CatRead)
def read_cat(cat_id: int, db: Session = Depends(get_db)):
    cat = get_cat(db, cat_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")
    return cat

@router.patch("/{cat_id}/salary", response_model=CatRead)
def update_cat_salary_endpoint(cat_id: int, salary_update: CatUpdateSalary, db: Session = Depends(get_db)):
    cat = update_cat_salary(db, cat_id, salary_update.salary)
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")
    return cat

@router.delete("/{cat_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cat_endpoint(cat_id: int, db: Session = Depends(get_db)):
    success = delete_cat(db, cat_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cat not found")
