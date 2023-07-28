from uuid import uuid4
from sqlalchemy import Column, Integer, String, Date, Boolean, Enum, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from src.models import Base
import enum

class PaymentMethod(enum.Enum):
    Card = 1
    UPI = 2
    Online = 3
    
class Status(enum.Enum):
    Success = 1
    Failed = 2
    NotFound = 3

class Payments(Base):
    __tablename__ = "payments"
    payment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4 )
    userid = Column(UUID(as_uuid=True), ForeignKey("profile.profile_id"))
    payment_method = Column(Enum(PaymentMethod))
    amount = Column(Integer)
    points = Column(Integer)
    status = Column(Enum(Status))
    created_at = Column(Date)
    
    