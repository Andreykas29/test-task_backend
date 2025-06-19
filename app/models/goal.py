from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    mission_id = Column(Integer, ForeignKey("missions.id"))
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    notes = Column(String, default="")
    is_done = Column(Boolean, default=False)

    mission = relationship("Mission", back_populates="goals")
