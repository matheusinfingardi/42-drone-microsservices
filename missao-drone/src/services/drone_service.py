# app/application/drone_service.py
from src.core.drone import Drone
from src.core.interfaces.drone_repository import DroneRepository
from src.infrastructure.mavsdk_client import MAVSDKClient
from src.infrastructure.supabase_client import get_supabase_client

class DroneService:
    def __init__(self, drone: Drone, drone_repository: DroneRepository):
        self.drone = drone
        self.drone_repository = drone_repository
        self.mavsdk_client = MAVSDKClient(drone.id)

    async def connect_drone(self):
        try:
            await self.mavsdk_client.connect()
            self.drone.is_armed = await self.mavsdk_client.is_connected()
            # Salvar o status no banco de dados
            await self.drone_repository.save(self.drone)
            return f"Drone {self.drone.id} conectado."
        except Exception as e:
            return f"Erro ao conectar o drone: {str(e)}"

    async def arm_drone(self):
        try:
            await self.mavsdk_client.arm_drone()
            self.drone.is_armed = True
            await self.drone_repository.save(self.drone)
            return f"Drone {self.drone.id} armado."
        except Exception as e:
            return f"Erro ao armar o drone: {str(e)}"

    async def disarm_drone(self):
        try:
            await self.mavsdk_client.disarm_drone()
            self.drone.is_armed = False
            await self.drone_repository.save(self.drone)
            return f"Drone {self.drone.id} desarmado."
        except Exception as e:
            return f"Erro ao desarmar o drone: {str(e)}"
