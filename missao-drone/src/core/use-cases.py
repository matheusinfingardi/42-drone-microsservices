from src.core.drone import Drone
from src.core.interfaces.drone_repository import DroneRepository

class ConnectDrone:
    def __init__(self, repo: DroneRepository):
        self.repo = repo

    async def execute(self, drone: Drone) -> Drone:
        # Lógica de conexão
        # Simular uma conexão
        drone.is_armed = False
        return await self.repo.save(drone)

class ArmDrone:
    def __init__(self, repo: DroneRepository):
        self.repo = repo

    async def execute(self, drone: Drone) -> Drone:
        drone.is_armed = True
        return await self.repo.save(drone)

class DisarmDrone:
    def __init__(self, repo: DroneRepository):
        self.repo = repo

    async def execute(self, drone: Drone) -> Drone:
        drone.is_armed = False
        return await self.repo.save(drone)
