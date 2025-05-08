from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import backref, relationship
from datetime import datetime, timezone
from src.model.base import Base
from src.model.payments import Payments
from src.model.participant_raffle import ParticipantRaffle
from src.model.participant_raffle_number import ParticipantRaffleNumber

class Participant(Base):

    __tablename__ = 'participant'

    cpf = Column(String(15), primary_key=True)
    whatsapp = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    
    payments = relationship(Payments, backref=backref('participant'))
    participant_raffle = relationship(ParticipantRaffle, backref=backref('participant'))
    participant_raffle_number = relationship(ParticipantRaffleNumber, backref=backref('participant'))