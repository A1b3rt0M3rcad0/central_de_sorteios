from src.infra import SessionLocal
from src.model.participant_raffle_number import ParticipantRaffleNumber
from typing import Dict

class ParticipantRaffleNumberController:

    @staticmethod
    def create_participant_raffle_number(participant_cpf: str, raffle_numbers_id: int, raffle_id: int, payment_id: int) -> Dict:
        with SessionLocal() as session:
            participant_raffle_number = ParticipantRaffleNumber(
                participant_cpf=participant_cpf,
                raffle_numbers_id=raffle_numbers_id,
                raffle_id=raffle_id,
                payment_id=payment_id
            )
            session.add(participant_raffle_number)
            session.commit()
            return {"message": "Participant raffle number created successfully."}

    @staticmethod
    def get_participant_raffle_number(participant_cpf: str, raffle_numbers_id: int, raffle_id: int, payment_id: int) -> Dict:
        with SessionLocal() as session:
            participant_raffle_number = session.query(ParticipantRaffleNumber).filter_by(
                participant_cpf=participant_cpf,
                raffle_numbers_id=raffle_numbers_id,
                raffle_id=raffle_id,
                payment_id=payment_id
            ).first()
            if participant_raffle_number:
                return {
                    "participant_cpf": participant_raffle_number.participant_cpf,
                    "raffle_numbers_id": participant_raffle_number.raffle_numbers_id,
                    "raffle_id": participant_raffle_number.raffle_id,
                    "payment_id": participant_raffle_number.payment_id
                }
            else:
                return {"message": "Participant raffle number not found."}

    @staticmethod
    def update_participant_raffle_number(participant_cpf: str, raffle_numbers_id: int, raffle_id: int, payment_id: int) -> Dict:
        with SessionLocal() as session:
            participant_raffle_number = session.query(ParticipantRaffleNumber).filter_by(
                participant_cpf=participant_cpf,
                raffle_numbers_id=raffle_numbers_id,
                raffle_id=raffle_id,
                payment_id=payment_id
            ).first()
            if participant_raffle_number:
                # Assuming you want to update something here
                participant_raffle_number.raffle_numbers_id = raffle_numbers_id
                participant_raffle_number.raffle_id = raffle_id
                participant_raffle_number.payment_id = payment_id
                session.commit()
                return {"message": "Participant raffle number updated successfully."}
            else:
                return {"message": "Participant raffle number not found."}

    @staticmethod
    def delete_participant_raffle_number(participant_cpf: str, raffle_numbers_id: int, raffle_id: int, payment_id: int) -> Dict:
        with SessionLocal() as session:
            participant_raffle_number = session.query(ParticipantRaffleNumber).filter_by(
                participant_cpf=participant_cpf,
                raffle_numbers_id=raffle_numbers_id,
                raffle_id=raffle_id,
                payment_id=payment_id
            ).first()
            if participant_raffle_number:
                session.delete(participant_raffle_number)
                session.commit()
                return {"message": "Participant raffle number deleted successfully."}
            else:
                return {"message": "Participant raffle number not found."}