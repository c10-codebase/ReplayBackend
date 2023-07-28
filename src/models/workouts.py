from uuid import uuid4
from sqlalchemy import Column, Integer, String, Date, Boolean, Sequence, Text, ForeignKey, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from src.models import Base
import enum
from passlib.hash import bcrypt

class Results(enum.Enum):
    Started = 1
    InProgress = 2
    Completed = 3
    
class Workout(Base):
    __tablename__ = "workout"
    workout_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4 )
    userid = Column(UUID(as_uuid=True), ForeignKey("profile.profile_id"))
    name = Column(Text)
    points = Column(Integer)
    duration = Column(Integer)
    action = Column(Text)
    isFav = Column(Boolean)
    DOB = Column(Date)
    results = Column(Enum(Results))
    points = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_at = Column(DateTime)