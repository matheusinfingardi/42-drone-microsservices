# src/adapters/repositories/drone_repository.py

from mavsdk import System
from src.domain.repositories.drone_interface import DroneInterface
from src.settings import settings

class DroneRepository(DroneInterface):
    async def connect(self, drone_id: str) -> bool:
        # Busca o endereço do drone baseado no drone_id no Supabase
        response = settings.supabase.table("drones").select("address").eq("drone_id", drone_id).single().execute()

        if response.status_code != 200:
            raise Exception("Erro ao buscar endereço do drone no Supabase.")
        
        address = response.data.get("address")
        
        if not address:
            raise Exception(f"Endereço do drone com id {drone_id} não encontrado no banco de dados.")
        
        # Conectar ao drone
        drone = System()
        await drone.connect(system_address=address)
        
        # Espera pela conexão
        async for state in drone.core.connection_state():
            if state.is_connected:
                return True
        
        return False
