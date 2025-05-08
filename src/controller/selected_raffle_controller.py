from src.infra import SessionLocal
from src.model.selected_raffle import SelectedRaffle
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional, Dict


class SelectedRaffleController:

    @staticmethod
    def create_selected_raffle(raffle_id: int, active: bool = False) -> Dict:
        with SessionLocal() as session:
            try:
                selected = SelectedRaffle(
                    raffle_id=raffle_id,
                    active=active
                )
                session.add(selected)
                session.commit()
                return {"message": "SelectedRaffle created successfully.", "id": selected.id}
            except SQLAlchemyError as e:
                session.rollback()
                return {"error": str(e)}

    @staticmethod
    def get_selected_raffle_by_id(selected_id: int) -> Optional[Dict]:
        with SessionLocal() as session:
            selected = session.query(SelectedRaffle).filter_by(id=selected_id).first()
            if selected:
                return {
                    "id": selected.id,
                    "raffle_id": selected.raffle_id,
                    "active": selected.active
                }
            return None

    @staticmethod
    def list_selected_raffles() -> List[Dict]:
        with SessionLocal() as session:
            selected_list = session.query(SelectedRaffle).all()
            return [{
                "id": s.id,
                "raffle_id": s.raffle_id,
                "active": s.active
            } for s in selected_list]

    @staticmethod
    def update_selected_raffle(selected_id: int,
                               raffle_id: Optional[int] = None,
                               active: Optional[bool] = None) -> Dict:
        with SessionLocal() as session:
            selected = session.query(SelectedRaffle).filter_by(id=selected_id).first()
            if selected:
                if raffle_id is not None:
                    selected.raffle_id = raffle_id
                if active is not None:
                    selected.active = active
                session.commit()
                return {"message": "SelectedRaffle updated successfully."}
            return {"message": "SelectedRaffle not found."}

    @staticmethod
    def delete_selected_raffle(selected_id: int) -> Dict:
        with SessionLocal() as session:
            selected = session.query(SelectedRaffle).filter_by(id=selected_id).first()
            if selected:
                session.delete(selected)
                session.commit()
                return {"message": "SelectedRaffle deleted successfully."}
            return {"message": "SelectedRaffle not found."}