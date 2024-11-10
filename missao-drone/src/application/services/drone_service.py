import asyncio
from src.infrastructure.mavsdk_client import MAVSDKClient
from src.infrastructure.supabase_client import get_supabase_client
from src.core.drone import Drone

class DroneService:
    def __init__(self, drone: Drone):
        self.drone = drone
        self.mavsdk_client = MAVSDKClient(drone.id)

    async def connect_drone(self):
        """
        Conecta ao drone e atualiza o status no banco de dados.
        """
        await self.mavsdk_client.connect()
        self.drone.is_armed = await self.mavsdk_client.is_connected()

        # Atualizar status no banco de dados (usando Supabase)
        supabase = get_supabase_client()
        supabase.from_('drones').update({'is_armed': self.drone.is_armed}).match({'id': self.drone.id})

    async def arm_drone(self):
        """
        Arma o drone e atualiza no banco de dados.
        """
        await self.mavsdk_client.arm_drone()
        self.drone.is_armed = True

        supabase = get_supabase_client()
        supabase.from_('drones').update({'is_armed': self.drone.is_armed}).match({'id': self.drone.id})

    async def disarm_drone(self):
        """
        Desarma o drone e atualiza no banco de dados.
        """
        await self.mavsdk_client.disarm_drone()
        self.drone.is_armed = False

        supabase = get_supabase_client()
        supabase.from_('drones').update({'is_armed': self.drone.is_armed}).match({'id': self.drone.id})
