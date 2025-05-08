from src.infra import SessionLocal
from src.model.raffle_numbers import RaffleNumbers
from typing import Dict, List, Optional
from sqlalchemy.exc import SQLAlchemyError


class RaffleNumbersController:

    @staticmethod
    def create_raffle_number(raffle_id: int, number: int) -> Dict:
        with SessionLocal() as session:
            try:
                raffle_number = RaffleNumbers(
                    raffle_id=raffle_id,
                    number=number
                )
                session.add(raffle_number)
                session.commit()
                return {"message": "Raffle number created successfully.", "id": raffle_number.id}
            except SQLAlchemyError as e:
                session.rollback()
                return {"error": str(e)}

    @staticmethod
    def get_raffle_number_by_id(raffle_number_id: int) -> Optional[Dict]:
        with SessionLocal() as session:
            raffle_number = session.query(RaffleNumbers).filter_by(id=raffle_number_id).first()
            if raffle_number:
                return {
                    "id": raffle_number.id,
                    "raffle_id": raffle_number.raffle_id,
                    "number": raffle_number.number,
                    "created_at": raffle_number.created_at.isoformat()
                }
            return None

    @staticmethod
    def list_raffle_numbers_by_raffle(raffle_id: int) -> List[Dict]:
        with SessionLocal() as session:
            numbers = session.query(RaffleNumbers).filter_by(raffle_id=raffle_id).all()
            return [{
                "id": r.id,
                "raffle_id": r.raffle_id,
                "number": r.number,
                "created_at": r.created_at.isoformat()
            } for r in numbers]

    @staticmethod
    def update_raffle_number(raffle_number_id: int, number: int) -> Dict:
        with SessionLocal() as session:
            raffle_number = session.query(RaffleNumbers).filter_by(id=raffle_number_id).first()
            if raffle_number:
                raffle_number.number = number
                session.commit()
                return {"message": "Raffle number updated successfully."}
            return {"message": "Raffle number not found."}

    @staticmethod
    def delete_raffle_number(raffle_number_id: int) -> Dict:
        with SessionLocal() as session:
            raffle_number = session.query(RaffleNumbers).filter_by(id=raffle_number_id).first()
            if raffle_number:
                session.delete(raffle_number)
                session.commit()
                return {"message": "Raffle number deleted successfully."}
            return {"message": "Raffle number not found."}