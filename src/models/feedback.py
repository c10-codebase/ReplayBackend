from uuid import uuid4
from sqlalchemy import Column, Integer, String, Date, Boolean, Sequence, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from src.models import Base

class FeedBack(Base):
    __tablename__ = "feedback"
    feedback_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4 )
    game_id = Column(UUID(as_uuid=True), ForeignKey("games.game_id"))
    message = Column(Text)
    ratting = Column(Text)
    profile_id = Column(UUID(as_uuid=True), ForeignKey("profile.profile_id"))
    created_at = Column(Date)
    
    