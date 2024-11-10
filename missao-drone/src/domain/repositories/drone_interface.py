# src/domain/repositories/drone_interface.py

from abc import ABC, abstractmethod

class DroneInterface(ABC):
    @abstractmethod
    async def connect(self, address: str) -> bool:
        pass
