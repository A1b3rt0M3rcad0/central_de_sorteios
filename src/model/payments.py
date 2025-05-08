from sqlalchemy import Column, String, Integer, ForeignKey, Text, DECIMAL, DateTime
from datetime import datetime, timezone
from src.model.base import Base
from sqlalchemy.orm import relationship, backref
from src.model.participant_raffle_number import ParticipantRaffleNumber

class Payments(Base):

    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    participant_cpf = Column(String(15), ForeignKey('participant.cpf'), nullable=False)
    raffle_id = Column(Integer, ForeignKey('raffle.id'), nullable=False)
    payment_id = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    pix_qr_code = Column(Text, nullable=True)
    pix_qr_code_base64 = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    approved_at = Column(DateTime, default=datetime.now(timezone.utc))

    participant_raffle_number = relationship(ParticipantRaffleNumber, backref=backref('payments'))