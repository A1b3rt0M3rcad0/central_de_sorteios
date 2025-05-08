from src.model.base import Base
from sqlalchemy import Integer, DateTime, Column, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship, backref
from src.model.participant_raffle_number import ParticipantRaffleNumber

class RaffleNumbers(Base):

    __tablename__ = 'raffle_numbers'

    id = Column(Integer, primary_key=True)
    raffle_id = Column(Integer, ForeignKey('raffle.id'), nullable=False)
    number = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    participnat_raffle_number = relationship(ParticipantRaffleNumber, backref=backref('raffle_numbers'))