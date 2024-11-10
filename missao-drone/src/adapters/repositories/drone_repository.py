# src/adapters/repositories/drone_repository.py

from supabase import create_client
from src.settings import settings

class DroneRepository:
    def __init__(self):
        # Configuração do cliente do Supabase
        self.supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    async def get_drone_by_id(self, drone_id: str):
        # Busca na tabela 'drone' pelo 'drone_id'
        response = self.supabase.table('drone').select('*').eq('drone_id', drone_id).execute()

        if response.status_code == 200 and len(response.data) > 0:
            return response.data[0]  # Retorna o primeiro drone encontrado

        return None  # Se não encontrar nenhum drone com esse drone_id
