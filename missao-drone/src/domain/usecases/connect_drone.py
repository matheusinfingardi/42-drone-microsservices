# src/domain/usecases/connect_drone.py

from src.domain.repositories.drone_interface import DroneInterface

class ConnectDrone:
    def __init__(self, drone_repo: DroneInterface):
        self.drone_repo = drone_repo

    async def execute(self, drone_id: str) -> bool:
        return await self.drone_repo.connect(drone_id)
