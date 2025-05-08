#pylint:disable=W0611
from src.model.base import Base
from src.model.package import Package
from src.model.participant import Participant
from src.model.participant_raffle import ParticipantRaffle
from src.model.participant_raffle_number import ParticipantRaffleNumber
from src.model.payments import Payments
from src.model.raffle import Raffle
from src.model.raffle_numbers import RaffleNumbers
from src.model.selected_raffle import SelectedRaffle
from src import infra

Base.metadata.create_all(bind=infra.engine)