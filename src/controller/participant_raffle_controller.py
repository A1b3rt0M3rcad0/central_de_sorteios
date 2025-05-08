from src.infra import SessionLocal
from src.model.participant_raffle import ParticipantRaffle
from typing import Dict

class ParticipantRaffleController:

    @staticmethod
    def create_participant_raffle(participant_cpf: str, raffle_id: int) -> Dict:
        with SessionLocal() as session:
            participant_raffle = ParticipantRaffle(
                participant_cpf=participant_cpf,
                raffle_id=raffle_id
            )
            session.add(participant_raffle)
            session.commit()
            return {"message": "Participant raffle created successfully."}

    @staticmethod
    def get_participant_raffle(participant_cpf: str, raffle_id: int) -> Dict:
        with SessionLocal() as session:
            participant_raffle = session.query(ParticipantRaffle).filter_by(
                participant_cpf=participant_cpf,
                raffle_id=raffle_id
            ).first()
            if participant_raffle:
                return {
                    "participant_cpf": participant_raffle.participant_cpf,
                    "raffle_id": participant_raffle.raffle_id,
                    "created_at": participant_raffle.created_at
                }
            else:
                return {"message": "Participant raffle not found."}

    @staticmethod
    def update_participant_raffle(participant_cpf: str, raffle_id: int) -> Dict:
        with SessionLocal() as session:
            participant_raffle = session.query(ParticipantRaffle).filter_by(
                participant_cpf=participant_cpf,
                raffle_id=raffle_id
            ).first()
            if participant_raffle:
                # Assuming you want to update the `raffle_id` (you can add more fields to update here)
                participant_raffle.raffle_id = raffle_id
                session.commit()
                return {"message": "Participant raffle updated successfully."}
            else:
                return {"message": "Participant raffle not found."}

    @staticmethod
    def delete_participant_raffle(participant_cpf: str, raffle_id: int) -> Dict:
        with SessionLocal() as session:
            participant_raffle = session.query(ParticipantRaffle).filter_by(
                participant_cpf=participant_cpf,
                raffle_id=raffle_id
            ).first()
            if participant_raffle:
                session.delete(participant_raffle)
                session.commit()
                return {"message": "Participant raffle deleted successfully."}
            else:
                return {"message": "Participant raffle not found."}