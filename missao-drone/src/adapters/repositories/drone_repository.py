# src/adapters/repositories/drone_repository.py

from supabase import create_client
from src.settings import settings

class DroneRepository:
    def __init__(self):
        # Cria a conexão com o Supabase
        self.supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    # Método para obter dados do drone baseado no drone_id
    async def get_drone_by_id(self, drone_id: str):
        # Faz a consulta ao banco para buscar o drone com o drone_id
        response = self.supabase.table('drones').select('*').eq('drone_id', drone_id).execute()

        # Verifica se a resposta tem dados
        if response.data and len(response.data) > 0:
            return response.data[0]  # Retorna o primeiro drone encontrado
        else:
            return None  # Retorna None caso o drone não seja encontrado

    # Método para conectar ao drone
    async def connect_to_drone(self, drone_id: str):
        # Faz a consulta ao banco para verificar o status de conexão
        response = self.supabase.table('drones').select('connection_status').eq('drone_id', drone_id).execute()

        # Verifica se a resposta contém dados
        if response.data and len(response.data) > 0:
            # Atualiza o status de conexão no banco
            self.supabase.table('drones').update({"connection_status": "connected"}).eq('drone_id', drone_id).execute()
            return {"status": "connected", "drone_id": drone_id}
        else:
            return {"status": "failed", "error": "Drone não encontrado ou não pode ser conectado"}
