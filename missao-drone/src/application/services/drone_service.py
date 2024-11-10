import asyncio
from src.infrastructure.mavsdk_client import MAVSDKClient
from src.infrastructure.supabase_client import get_supabase_client
from src.core.drone import Drone
from supabase import Client

class DroneService:
    def __init__(self, drone: Drone):
        self.drone = drone
        self.mavsdk_client = MAVSDKClient(drone.id)

    async def connect_drone(self):
        """
        Conecta ao drone e atualiza o status no banco de dados.
        """
        try:
            # Conectar ao drone
            await self.mavsdk_client.connect()
            # Verificar se o drone está conectado
            self.drone.is_armed = await self.mavsdk_client.is_connected()

            # Atualizar status no banco de dados (usando Supabase)
            supabase: Client = get_supabase_client()
            response = supabase.from_('drones').update({'is_armed': self.drone.is_armed}).match({'id': self.drone.id}).execute()

            if response.status_code != 200:
                raise Exception(f"Erro ao atualizar o status no banco de dados: {response.message}")
            return f"Drone {self.drone.id} conectado e status atualizado no banco de dados."
        except Exception as e:
            raise Exception(f"Erro ao conectar o drone: {str(e)}")

    async def arm_drone(self):
        """
        Arma o drone e atualiza no banco de dados.
        """
        try:
            # Armar o drone
            await self.mavsdk_client.arm_drone()
            self.drone.is_armed = True

            # Atualizar o banco de dados
            supabase: Client = get_supabase_client()
            response = supabase.from_('drones').update({'is_armed': self.drone.is_armed}).match({'id': self.drone.id}).execute()

            if response.status_code != 200:
                raise Exception(f"Erro ao atualizar o status no banco de dados: {response.message}")
            return f"Drone {self.drone.id} armado e status atualizado no banco de dados."
        except Exception as e:
            raise Exception(f"Erro ao armar o drone: {str(e)}")

    async def disarm_drone(self):
        """
        Desarma o drone e atualiza no banco de dados.
        """
        try:
            # Desarmar o drone
            await self.mavsdk_client.disarm_drone()
            self.drone.is_armed = False

            # Atualizar o banco de dados
            supabase: Client = get_supabase_client()
            response = supabase.from_('drones').update({'is_armed': self.drone.is_armed}).match({'id': self.drone.id}).execute()

            if response.status_code != 200:
                raise Exception(f"Erro ao atualizar o status no banco de dados: {response.message}")
            return f"Drone {self.drone.id} desarmado e status atualizado no banco de dados."
        except Exception as e:
            raise Exception(f"Erro ao desarmar o drone: {str(e)}")
