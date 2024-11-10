from abc import ABC, abstractmethod
from src.core.drone import Drone

class DroneRepository(ABC):
    
    @abstractmethod
    async def save(self, drone: Drone) -> Drone:
        """Salva um drone no repositório."""
        pass

    @abstractmethod
    async def get(self, drone_id: str) -> Drone:
        """Recupera um drone do repositório pelo ID."""
        pass