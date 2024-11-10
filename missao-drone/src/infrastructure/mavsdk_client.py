import asyncio
from mavsdk import System

class MAVSDKClient:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.drone = System()

    async def connect(self):
        """
        Conecta ao drone utilizando o MAVSDK.
        """
        print(f"Conectando ao drone na porta: {self.connection_string}")
        await self.drone.connect(system_address=self.connection_string)

    async def arm_drone(self):
        """
        Arma o drone para voo.
        """
        print("Armando o drone...")
        await self.drone.action.arm()

    async def disarm_drone(self):
        """
        Desarma o drone.
        """
        print("Desarmando o drone...")
        await self.drone.action.disarm()

    async def is_connected(self) -> bool:
        """
        Verifica se o drone está conectado.
        """
        async for health in self.drone.telemetry.health():
            if health.is_armed:
                return True
        return False
