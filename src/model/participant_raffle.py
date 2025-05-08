from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime, timezone
from src.model.base import Base

class ParticipantRaffle(Base):

    __tablename__ = 'participant_raffle'
    participant_cpf = Column(String(15), ForeignKey('participant.cpf'), primary_key=True)
    raffle_id = Column(Integer, ForeignKey('raffle.id'), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    