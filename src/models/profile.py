from uuid import uuid4
from sqlalchemy import Column, Integer, String, Date, Boolean, Sequence, Text, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from models import Base
import enum
from passlib.hash import bcrypt

class Sex(enum.Enum):
    male = 1
    female = 2
    others = 3
    
class Profile(Base):
    __tablename__ = "profile"
    profileid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4 )
    username = Column(Text)
    email = Column(Text,unique=True)
    phone = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    DOB = Column(Date)
    sex = Column(Enum(Sex))
    password = Column(Text)
    photo = Column(Text)
    points = Column(Integer)
    created_at = Column(Date)
    
    
    
    def __init__(self, username, password, email,phone):
        self.email = email
        self.password = bcrypt.encrypt(password)
        self.username = username
        self.phone = phone
    
    def validate_password(self, password):
        return bcrypt.verify(password, self.password)
    
    def set_password(self,password):
        self.password = bcrypt.encrypt(password)
