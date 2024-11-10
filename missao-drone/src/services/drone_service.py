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
                # Garantindo que o retorno seja um dicionário serializável
                return data if isinstance(data, dict) else data.__dict__
            else:
                logging.warning(f"Nenhum drone encontrado com drone_id: {drone_id}")
                return {"message": "Drone não encontrado", "drone_id": drone_id}

        except Exception as e:
            # Log de erro
            logging.error(f"Erro ao consultar drone com drone_id {drone_id}: {e}")
            return {"error": "Erro interno ao consultar o drone"}
