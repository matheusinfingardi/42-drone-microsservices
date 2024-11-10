# src/app/interfaces/api.py
from fastapi import FastAPI
from src.services.drone_service import DroneService

app = FastAPI()

# Endpoint para obter um drone
@app.get("/drone/{drone_id}")
async def get_drone(drone_id: int):
    drone_service = DroneService()
    drone = drone_service.get_drone_by_id(drone_id)
    return drone

# Endpoint para criar um drone (ou outro serviço)
@app.post("/drone/")
async def create_drone(drone_data: dict):
    drone_service = DroneService()
    new_drone = drone_service.create_drone(drone_data)
    return new_drone
