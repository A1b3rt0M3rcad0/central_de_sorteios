from sqlalchemy import Integer, ForeignKey, DECIMAL, DateTime, Column
from datetime import datetime, timezone
from src.model.base import Base

class Package(Base):

    __tablename__ = 'package'

    id = Column(Integer, primary_key=True)
    raffle_id = Column(Integer, ForeignKey('raffle.id'), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))