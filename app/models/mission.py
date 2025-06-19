from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("cats.id"), nullable=True)  
    status = Column(String, default="active")  
    cat = relationship("Cat", back_populates="missions")
    goals = relationship("Goal", back_populates="mission", cascade="all, delete-orphan")
