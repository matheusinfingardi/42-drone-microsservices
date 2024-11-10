from fastapi import FastAPI
from src.services.drone_service import DroneService

app = FastAPI()

# Endpoint para obter um drone
@app.get("/drone/{drone_id}")
async def get_drone(drone_id: int):
    """
    Endpoint para consultar um drone pelo drone_id
    """
    drone_service = DroneService()
    drone = await drone_service.get_drone_by_id(drone_id)  # Ajuste para consulta assíncrona
    return drone

# Endpoint para criar um drone
@app.post("/drone/")
async def create_drone(drone_data: dict):
    """
    Endpoint para criar um novo drone
    """
    drone_service = DroneService()
    new_drone = await drone_service.create_drone(drone_data)  # Ajuste para operação assíncrona
    return new_drone
