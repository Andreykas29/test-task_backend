from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float
from app.db import Base

class Cat(Base):
    __tablename__ = "cats"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    experience: Mapped[int] = mapped_column(Integer)
    breed: Mapped[str] = mapped_column(String)
    salary: Mapped[float] = mapped_column(Float)

    missions = relationship("Mission", back_populates="cat")
