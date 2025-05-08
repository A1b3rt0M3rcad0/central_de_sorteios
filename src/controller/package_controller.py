from src.infra import SessionLocal
from src.model.package import Package
from decimal import Decimal
from typing import Dict, List, Optional

class PackageController:

    @staticmethod
    def create_package(raffle_id: int, price: Decimal) -> Dict:
        try:
            # Inicia uma sessão com o banco de dados
            with SessionLocal() as session:
                # Cria o objeto Package
                new_package = Package(raffle_id=raffle_id, price=price)
                
                # Adiciona o novo pacote à sessão
                session.add(new_package)
                
                # Realiza o commit para salvar no banco
                session.commit()
                
                # Retorna o resultado da operação, incluindo o id do novo pacote
                return {
                    "success": True,
                    "message": "Package created successfully",
                    "package_id": new_package.id
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
    def get_all_packages() -> List[Dict]:
        try:
            # Inicia uma sessão com o banco de dados
            with SessionLocal() as session:
                # Consulta todos os pacotes
                packages = session.query(Package).all()
                
                # Retorna todos os pacotes como uma lista de dicionários
                return [{
                    "id": package.id,
                    "raffle_id": package.raffle_id,
                    "price": str(package.price)
                } for package in packages]
        
        except Exception as e:
            # Retorna o erro, caso ocorra
            return [{
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }]
    
    @staticmethod
    def get_package_by_id(package_id: int) -> Optional[Dict]:
        try:
            # Inicia uma sessão com o banco de dados
            with SessionLocal() as session:
                # Consulta um pacote pelo ID
                package = session.query(Package).filter(Package.id == package_id).first()
                
                if package:
                    # Retorna o pacote encontrado como um dicionário
                    return {
                        "id": package.id,
                        "raffle_id": package.raffle_id,
                        "price": str(package.price)
                    }
                else:
                    # Retorna uma mensagem de pacote não encontrado
                    return {
                        "success": False,
                        "message": "Package not found"
                    }
        
        except Exception as e:
            # Retorna o erro, caso ocorra
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }
    
    @staticmethod
    def update_package(package_id: int, raffle_id: Optional[int] = None, price: Optional[Decimal] = None) -> Dict:
        try:
            # Inicia uma sessão com o banco de dados
            with SessionLocal() as session:
                # Busca o pacote pelo ID
                package = session.query(Package).filter(Package.id == package_id).first()
                
                if not package:
                    return {
                        "success": False,
                        "message": "Package not found"
                    }
                
                # Atualiza os campos se forem fornecidos
                if raffle_id:
                    package.raffle_id = raffle_id
                if price is not None:
                    package.price = price
                
                # Commit para salvar as alterações
                session.commit()
                
                return {
                    "success": True,
                    "message": "Package updated successfully"
                }
        
        except Exception as e:
            # Retorna o erro, caso ocorra
            session.rollback()
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }
    
    @staticmethod
    def delete_package(package_id: int) -> Dict:
        try:
            # Inicia uma sessão com o banco de dados
            with SessionLocal() as session:
                # Busca o pacote pelo ID
                package = session.query(Package).filter(Package.id == package_id).first()
                
                if not package:
                    return {
                        "success": False,
                        "message": "Package not found"
                    }
                
                # Deleta o pacote
                session.delete(package)
                session.commit()
                
                return {
                    "success": True,
                    "message": "Package deleted successfully"
                }
        
        except Exception as e:
            # Retorna o erro, caso ocorra
            session.rollback()
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }