# src/adapters/repositories/drone_repository.py

from supabase import create_client
from src.settings import settings

class DroneRepository:
    def __init__(self):
        self.supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    # Método para obter dados de um drone específico baseado no 'drone_id'
    async def get_drone_by_id(self, drone_id: str):
        # Consulta o drone com base no 'drone_id'
        response = self.supabase.table('drones').select('*').eq('drone_id', drone_id).execute()

        if response.status_code == 200 and len(response.data) > 0:
            return response.data[0]  # Retorna o drone encontrado
        else:
            return None  # Retorna None se o drone não for encontrado
    
    # Método para simular a conexão com o drone (pode ser uma lógica com MAVSDK ou outro)
    async def connect_to_drone(self, drone_id: str):
        # Exemplo de lógica de conexão, pode ser modificado conforme sua implementação com MAVSDK
        # Aqui você pode implementar a lógica de conectar ao drone via MAVSDK, por exemplo
        response = self.supabase.table('drones').select('connection_status').eq('drone_id', drone_id).execute()

        if response.status_code == 200 and len(response.data) > 0:
            # Suponhamos que você conecte com sucesso aqui e altere o status
            # Atualizar o status de conexão no banco (exemplo)
            self.supabase.table('drones').update({"connection_status": "connected"}).eq('drone_id', drone_id).execute()
            return {"status": "connected", "drone_id": drone_id}
        else:
            return {"status": "failed", "error": "Drone não encontrado ou não pode ser conectado"}
