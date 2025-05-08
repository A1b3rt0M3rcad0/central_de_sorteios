from src.model.base import Base
from sqlalchemy import Integer, ForeignKey, Boolean, Column

class SelectedRaffle(Base):

    __tablename__ = 'selected_raffle'

    id = Column(Integer, primary_key=True)
    raffle_id = Column(Integer, ForeignKey('raffle.id'), nullable=False)
    active = Column(Boolean, nullable=False, default=False)