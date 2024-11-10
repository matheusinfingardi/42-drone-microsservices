import logging
from src.infrastructure.supabase_integration import get_supabase_client
from concurrent.futures import ThreadPoolExecutor
import asyncio

class DroneService:
    def __init__(self):
        # Inicializa o cliente do Supabase
        self.client = get_supabase_client()
        self.executor = ThreadPoolExecutor()

    async def get_drone_by_id(self, drone_id: int):
        """
        Consulta um drone pela coluna drone_id
        """
        logging.info(f"Consultando drone com drone_id: {drone_id}")
        
        try:
            # Uso de run_in_executor para operações síncronas em contexto assíncrono
            data = await asyncio.get_running_loop().run_in_executor(
                self.executor,
                lambda: self.client.table('drone').select('*').eq('drone_id', drone_id).single()
            )

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
            # Inserindo o novo drone usando run_in_executor para manter o código assíncrono
            response = await asyncio.get_running_loop().run_in_executor(
                self.executor,
                lambda: self.client.table('drone').insert(drone_data).execute()
            )
            
            if response.status_code == 201:
                logging.info(f"Drone criado com sucesso: {response.data}")
                return response.data
            else:
                logging.error(f"Erro ao criar drone: {response.error_message}")
                return None
        except Exception as e:
            logging.error(f"Erro ao tentar criar drone: {e}")
            return None
