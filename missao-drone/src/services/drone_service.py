import logging
from src.infrastructure.supabase_integration import get_supabase_client
from fastapi.encoders import jsonable_encoder  # Import do jsonable_encoder

class DroneService:
    def __init__(self):
        # Inicializa o cliente do Supabase
        self.client = get_supabase_client()

    def get_drone_by_id(self, drone_id: int):
        """
        Consulta um drone pela coluna drone_id de forma síncrona
        """
        logging.info(f"Consultando drone com drone_id: {drone_id}")
        
        try:
            # Consulta síncrona ao Supabase
            data = self.client.table('drone').select('*').eq('drone_id', drone_id).single()

            if data:
                logging.info(f"Resultado da consulta: {data}")
                # Serializando o resultado para garantir compatibilidade com JSON
                return jsonable_encoder(data)
            else:
                logging.warning(f"Nenhum drone encontrado com drone_id: {drone_id}")
                return {"message": "Drone não encontrado", "drone_id": drone_id}

        except Exception as e:
            # Log de erro
            logging.error(f"Erro ao consultar drone com drone_id {drone_id}: {e}")
            return {"error": "Erro interno ao consultar o drone"}
