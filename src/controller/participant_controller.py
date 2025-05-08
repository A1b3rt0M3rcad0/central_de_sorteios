from src.infra import SessionLocal
from src.model.participant import Participant
from typing import Dict, List, Optional

class ParticipantController:

    @staticmethod
    def create_participant(cpf: str, whatsapp: str) -> Dict:
        try:
            # Inicia uma sessão com o banco de dados
            with SessionLocal() as session:
                # Cria o objeto Participant
                new_participant = Participant(cpf=cpf, whatsapp=whatsapp)
                
                # Adiciona o novo participante à sessão
                session.add(new_participant)
                
                # Realiza o commit para salvar no banco
                session.commit()
                
                # Retorna o resultado da operação, incluindo o CPF do novo participante
                return {
                    "success": True,
                    "message": "Participant created successfully",
                    "cpf": new_participant.cpf
                }
        
        except Exception as e:
            # Se ocorrer qualquer erro, realiza o rollback da transação
            session.rollback()
            
            # Retorna o erro para a camada de serviço
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }

    @staticmethod
    def get_all_participants() -> List[Dict]:
        try:
            # Inicia uma sessão com o banco de dados
            with SessionLocal() as session:
                # Consulta todos os participantes
                participants = session.query(Participant).all()
                
                # Retorna todos os participantes como uma lista de dicionários
                return [{
                    "cpf": participant.cpf,
                    "whatsapp": participant.whatsapp,
                    "created_at": str(participant.created_at)
                } for participant in participants]
        
        except Exception as e:
            # Retorna o erro, caso ocorra
            return [{
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }]
    
    @staticmethod
    def get_participant_by_cpf(cpf: str) -> Optional[Dict]:
        try:
            # Inicia uma sessão com o banco de dados
            with SessionLocal() as session:
                # Consulta um participante pelo CPF
                participant = session.query(Participant).filter(Participant.cpf == cpf).first()
                
                if participant:
                    # Retorna o participante encontrado como um dicionário
                    return {
                        "cpf": participant.cpf,
                        "whatsapp": participant.whatsapp,
                        "created_at": str(participant.created_at)
                    }
                else:
                    # Retorna uma mensagem de participante não encontrado
                    return {
                        "success": False,
                        "message": "Participant not found"
                    }
        
        except Exception as e:
            # Retorna o erro, caso ocorra
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }
    
    @staticmethod
    def update_participant(cpf: str, whatsapp: Optional[str] = None) -> Dict:
        try:
            # Inicia uma sessão com o banco de dados
            with SessionLocal() as session:
                # Busca o participante pelo CPF
                participant = session.query(Participant).filter(Participant.cpf == cpf).first()
                
                if not participant:
                    return {
                        "success": False,
                        "message": "Participant not found"
                    }
                
                # Atualiza o campo do whatsapp se fornecido
                if whatsapp:
                    participant.whatsapp = whatsapp
                
                # Commit para salvar as alterações
                session.commit()
                
                return {
                    "success": True,
                    "message": "Participant updated successfully"
                }
        
        except Exception as e:
            # Retorna o erro, caso ocorra
            session.rollback()
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }
    
    @staticmethod
    def delete_participant(cpf: str) -> Dict:
        try:
            # Inicia uma sessão com o banco de dados
            with SessionLocal() as session:
                # Busca o participante pelo CPF
                participant = session.query(Participant).filter(Participant.cpf == cpf).first()
                
                if not participant:
                    return {
                        "success": False,
                        "message": "Participant not found"
                    }
                
                # Deleta o participante
                session.delete(participant)
                session.commit()
                
                return {
                    "success": True,
                    "message": "Participant deleted successfully"
                }
        
        except Exception as e:
            # Retorna o erro, caso ocorra
            session.rollback()
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }