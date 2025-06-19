from pydantic import BaseModel, Field

class CatBase(BaseModel):
    name: str = Field(...)
    experience: int = Field(..., ge=0)
    breed: str = Field(...)
    salary: float = Field(..., ge=0)

class CatCreate(CatBase):
    pass

class CatUpdateSalary(BaseModel):
    salary: float = Field(..., ge=0)

class CatRead(CatBase):
    id: int

    class Config:
        orm_mode = True  
