import logging
from src.infrastructure.supabase_integration import get_supabase_client

class DroneService:
    def __init__(self):
        # Inicializa o cliente do Supabase
        self.client = get_supabase_client()

    async def get_drone_by_id(self, drone_id: int):
        """
        Consulta um drone pela coluna drone_id
        """
        logging.info(f"Consultando drone com drone_id: {drone_id}")
        
        try:
            # Consultando o drone na tabela 'drone' pelo drone_id
            data = await self.client.table('drone').select('*').eq('drone_id', drone_id).single()

            if data:
                logging.info(f"Resultado da consulta: {data}")
            else:
                logging.warning(f"Nenhum drone encontrado com drone_id: {drone_id}")

            return data
        except Exception as e:
            # Log de erro
            logging.error(f"Erro ao consultar drone com drone_id {drone_id}: {e}")
            return None

    async def create_drone(self, drone_data: dict):
        """
        Cria um novo drone na base de dados
        """
        logging.info(f"Criando novo drone com os dados: {drone_data}")
        
        try:
            # Inserindo o novo drone na tabela
            response = await self.client.table('drone').insert(drone_data).execute()
            
            if response.status_code == 201:
                logging.info(f"Drone criado com sucesso: {response.data}")
                return response.data
            else:
                logging.error(f"Erro ao criar drone: {response.error_message}")
                return None
        except Exception as e:
            logging.error(f"Erro ao tentar criar drone: {e}")
            return None
