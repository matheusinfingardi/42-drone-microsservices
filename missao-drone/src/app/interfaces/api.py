# app/interfaces/api.py
from fastapi import FastAPI
from pydantic import BaseModel
from src.core.drone import Drone
from src.services.drone_service import DroneService
from src.infrastructure.supabase_client import get_supabase_client

app = FastAPI()

# Modelagem dos dados de entrada (JSON)
class DroneRequest(BaseModel):
    id: str
    name: str

# Instanciando o repositório e o serviço (normalmente, usaria injeção de dependência)
drone_repository = get_supabase_client()
drone_service = DroneService(Drone(id="", name=""), drone_repository)

@app.post("/drone/connect")
async def connect_drone(request: DroneRequest):
    drone = Drone(id=request.id, name=request.name)
    drone_service.drone = drone
    return await drone_service.connect_drone()

@app.post("/drone/arm")
async def arm_drone(request: DroneRequest):
    drone = Drone(id=request.id, name=request.name)
    drone_service.drone = drone
    return await drone_service.arm_drone()

@app.post("/drone/disarm")
async def disarm_drone(request: DroneRequest):
    drone = Drone(id=request.id, name=request.name)
    drone_service.drone = drone
    return await drone_service.disarm_drone()
