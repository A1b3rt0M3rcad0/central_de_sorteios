from src.infra import SessionLocal
from src.model.payments import Payments
from typing import Dict
from decimal import Decimal
from datetime import datetime

class PaymentsController:

    @staticmethod
    def create_payment(participant_cpf: str, raffle_id: int, payment_id: str, status: str, amount: Decimal, pix_qr_code_base64: str) -> Dict:
        with SessionLocal() as session:
            payment = Payments(
                participant_cpf=participant_cpf,
                raffle_id=raffle_id,
                payment_id=payment_id,
                status=status,
                amount=amount,
                pix_qr_code_base64=pix_qr_code_base64
            )
            session.add(payment)
            session.commit()
            return {"message": "Payment created successfully."}

    @staticmethod
    def get_payment(payment_id: str) -> Dict:
        with SessionLocal() as session:
            payment = session.query(Payments).filter_by(payment_id=payment_id).first()
            if payment:
                return {
                    "id": payment.id,
                    "participant_cpf": payment.participant_cpf,
                    "raffle_id": payment.raffle_id,
                    "payment_id": payment.payment_id,
                    "status": payment.status,
                    "amount": str(payment.amount),
                    "pix_qr_code": payment.pix_qr_code,
                    "pix_qr_code_base64": payment.pix_qr_code_base64,
                    "created_at": payment.created_at,
                    "approved_at": payment.approved_at
                }
            return {"message": "Payment not found."}

    @staticmethod
    def update_payment(payment_id: str, status: str, amount: Decimal, approved_at: datetime) -> Dict:
        with SessionLocal() as session:
            payment = session.query(Payments).filter_by(payment_id=payment_id).first()
            if payment:
                payment.status = status
                payment.amount = amount
                payment.approved_at = approved_at
                session.commit()
                return {"message": "Payment updated successfully."}
            return {"message": "Payment not found."}

    @staticmethod
    def delete_payment(payment_id: str) -> Dict:
        with SessionLocal() as session:
            payment = session.query(Payments).filter_by(payment_id=payment_id).first()
            if payment:
                session.delete(payment)
                session.commit()
                return {"message": "Payment deleted successfully."}
            return {"message": "Payment not found."}