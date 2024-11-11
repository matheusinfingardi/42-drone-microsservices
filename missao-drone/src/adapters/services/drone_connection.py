from mavsdk import System
import asyncio

async def connect_to_drone_real(drone_id: str) -> dict:
    """Conexão com o drone real"""
    connection_url = "udp://:14550"  # Ajuste conforme necessário

    drone = System()
    await drone.connect(system_address=connection_url)

    async for state in drone.core.connection_status():
        if state.is_connected:
            return {"message": f"Drone {drone_id} conectado com sucesso!", "status": "success"}
    return {"message": f"Falha ao conectar com o drone {drone_id}.", "status": "error"}

async def connect_to_sitl(drone_id: str) -> dict:
    """Conexão com o simulador SITL"""
    connection_url = "udp://:14540"  # Ajuste conforme necessário

    drone = System()
    await drone.connect(system_address=connection_url)

    async for state in drone.core.connection_status():
        if state.is_connected:
            return {"message": f"Simulador SITL {drone_id} conectado com sucesso!", "status": "success"}
    return {"message": f"Falha ao conectar com o simulador SITL {drone_id}.", "status": "error"}
