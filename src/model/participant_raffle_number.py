from sqlalchemy import String, Integer, Column, ForeignKey
from src.model.base import Base

class ParticipantRaffleNumber(Base):

    __tablename__ = 'participant_raffle_number'

    participant_cpf = Column(String(15), ForeignKey('participant.cpf'), primary_key=True)
    raffle_numbers_id = Column(Integer, ForeignKey('raffle_numbers.id'), primary_key=True)
    raffle_id = Column(Integer, ForeignKey('raffle.id'), primary_key=True)
    payment_id = Column(Integer, ForeignKey('payments.id'), primary_key=True)