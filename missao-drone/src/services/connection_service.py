from src.adapters.services.drone_connection import connect_to_sitl, connect_to_drone_real
from src.adapters.repositories.drone_repository import DroneRepository

class ConnectionService:
    def __init__(self, drone_repository: DroneRepository):
        self.drone_repository = drone_repository

    async def connect_drone(self, drone_id: str) -> dict:
        """Decide a conexão com base no tipo de drone (real ou SITL)"""
        # Obtenha o drone do repositório
        drone = await self.drone_repository.get_drone_by_id(drone_id)

        if not drone:
            return {"message": "Drone não encontrado", "status": "error"}

        # Verifica o tipo de conexão do drone
        if drone["connection_type"] == "sitl":
            return await connect_to_sitl(drone["drone_id"])
        elif drone["connection_type"] == "tty":
            return await connect_to_drone_real(drone["drone_id"])
        else:
            return {"message": "Tipo de conexão inválido", "status": "error"}
