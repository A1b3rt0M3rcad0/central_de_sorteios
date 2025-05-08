from sqlalchemy import Column, Integer, DECIMAL, DateTime, String
from datetime import datetime, timezone
from src.model.base import Base
from sqlalchemy.orm import backref, relationship
from src.model.payments import Payments
from src.model.selected_raffle import SelectedRaffle
from src.model.participant_raffle import ParticipantRaffle
from src.model.raffle_numbers import RaffleNumbers
from src.model.participant_raffle_number import ParticipantRaffleNumber

class Raffle(Base):

    __tablename__ = 'raffle'

    id = Column(Integer, primary_key=True)
    n_numbers = Column(Integer, nullable=False, default=100_000)
    price_per_number = Column(DECIMAL(10, 2), nullable=False)
    numbers_sold = Column(Integer, nullable=False, default=0)
    name = Column(String(100), nullable=False, default=' ')
    description = Column(String(100), nullable=False, default=' ')
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    payments = relationship(Payments, backref=backref('raffle'))
    selected_raffle = relationship(SelectedRaffle, backref=backref('raffle'))
    participant_raffle = relationship(ParticipantRaffle, backref=backref('raffle'))
    raffle_numbers = relationship(RaffleNumbers, backref=backref('raffle'))
    participant_raffle_number = relationship(ParticipantRaffleNumber, backref=backref('raffle'))