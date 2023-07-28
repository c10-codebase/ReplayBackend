from uuid import uuid4
from sqlalchemy import Column, Integer, String, Date, Boolean, Sequence, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from src.models import Base

class Games(Base):
    __tablename__ = "games"
    game_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4 )
    categery = Column(Text)
    cat_image = Column(Text)
    name = Column(Text)
    unity_path = Column(Text)
    points = Column(Integer)
    activity_json = Column(Text)
    
    




