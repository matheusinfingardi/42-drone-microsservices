# src/services/drone_service.py
from src.infrastructure.supabase_integration import get_supabase_client

class DroneService:
    def __init__(self):
        self.client = get_supabase_client()
        self.table = self.client.table("drones")  # Suponha que a tabela se chame "drones"
    
    def get_drone_by_id(self, drone_id: int):
        # Aqui consultamos o Supabase usando a ID do drone
        response = self.table.select("*").eq("id", drone_id).execute()
        if response.data:
            return response.data[0]
        return None
    
    def create_drone(self, drone_data: dict):
        # Aqui inserimos um novo drone no banco de dados
        response = self.table.insert(drone_data).execute()
        return response.data
