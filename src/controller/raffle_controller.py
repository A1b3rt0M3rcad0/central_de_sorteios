from src.infra import SessionLocal
from src.model.raffle import Raffle
from typing import List, Optional, Dict
from sqlalchemy.exc import SQLAlchemyError


class RaffleController:

    @staticmethod
    def create_raffle(n_numbers: int, price_per_number: float, name: str, description: str) -> Dict:
        with SessionLocal() as session:
            try:
                raffle = Raffle(
                    n_numbers=n_numbers,
                    price_per_number=price_per_number,
                    name=name,
                    description=description
                )
                session.add(raffle)
                session.commit()
                return {"message": "Raffle created successfully.", "id": raffle.id}
            except SQLAlchemyError as e:
                session.rollback()
                return {"error": str(e)}

    @staticmethod
    def get_raffle_by_id(raffle_id: int) -> Optional[Dict]:
        with SessionLocal() as session:
            raffle = session.query(Raffle).filter_by(id=raffle_id).first()
            if raffle:
                return {
                    "id": raffle.id,
                    "n_numbers": raffle.n_numbers,
                    "price_per_number": float(raffle.price_per_number),
                    "numbers_sold": raffle.numbers_sold,
                    "name": raffle.name,
                    "description": raffle.description,
                    "created_at": raffle.created_at.isoformat()
                }
            return None

    @staticmethod
    def list_raffles() -> List[Dict]:
        with SessionLocal() as session:
            raffles = session.query(Raffle).all()
            return [{
                "id": r.id,
                "n_numbers": r.n_numbers,
                "price_per_number": float(r.price_per_number),
                "numbers_sold": r.numbers_sold,
                "name": r.name,
                "description": r.description,
                "created_at": r.created_at.isoformat()
            } for r in raffles]

    @staticmethod
    def update_raffle(raffle_id: int, name: Optional[str] = None,
                      description: Optional[str] = None,
                      n_numbers: Optional[int] = None,
                      price_per_number: Optional[float] = None) -> Dict:
        with SessionLocal() as session:
            raffle = session.query(Raffle).filter_by(id=raffle_id).first()
            if raffle:
                if name is not None:
                    raffle.name = name
                if description is not None:
                    raffle.description = description
                if n_numbers is not None:
                    raffle.n_numbers = n_numbers
                if price_per_number is not None:
                    raffle.price_per_number = price_per_number
                session.commit()
                return {"message": "Raffle updated successfully."}
            return {"message": "Raffle not found."}

    @staticmethod
    def delete_raffle(raffle_id: int) -> Dict:
        with SessionLocal() as session:
            raffle = session.query(Raffle).filter_by(id=raffle_id).first()
            if raffle:
                session.delete(raffle)
                session.commit()
                return {"message": "Raffle deleted successfully."}
            return {"message": "Raffle not found."}